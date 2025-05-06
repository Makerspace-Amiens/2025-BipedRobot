import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import patches

class BipedRobot:
    def __init__(self):
        # --- Paramètres biomécaniques (pour l'instant) ---
        self.l_thigh = 0.47
        self.l_shank = 0.45
        self.l_foot = 0.25
        self.h_hip = 0.92
        self.ground_level = 0
        self.step_frequency = 1.1
        self.cycle_time = 1.0 / self.step_frequency
        self.swing_phase_ratio = 0.4
        self.double_support_ratio = 0.15
        self.step_length = 0.65
        self.gait_cycle = self.step_length * 2
        self.foot_clearance = 0.12
        self.pelvic_tilt_amplitude = 0.06
        self.pelvic_rotation_amplitude = 0.03
        self.pelvic_sway_amplitude = 0.01
        self.horizontal_speed = self.step_length * self.step_frequency
        self.contact_x_right = None
        self.contact_x_left = None
        self.global_x_position = 0.0

    def get_gait_phase_progress(self, t, leg='right'):
        phase_normalized = (t % self.cycle_time) / self.cycle_time
        offset = 0.5 if leg == 'left' else 0
        adjusted_phase = (phase_normalized + offset) % 1.0

        if adjusted_phase < 0.05:
            return 'initial_contact', adjusted_phase / 0.05
        elif adjusted_phase < 0.12:
            return 'loading_response', (adjusted_phase - 0.05) / 0.07
        elif adjusted_phase < 0.30:
            return 'mid_stance', (adjusted_phase - 0.12) / 0.18
        elif adjusted_phase < 0.45:
            return 'terminal_stance', (adjusted_phase - 0.30) / 0.15
        elif adjusted_phase < 0.55:
            return 'pre_swing', (adjusted_phase - 0.45) / 0.10
        elif adjusted_phase < 0.65:
            return 'initial_swing', (adjusted_phase - 0.55) / 0.10
        elif adjusted_phase < 0.80:
            return 'mid_swing', (adjusted_phase - 0.65) / 0.15
        elif adjusted_phase < 0.92:
            return 'terminal_swing', (adjusted_phase - 0.80) / 0.12
        elif adjusted_phase < 0.97:
            return 'swing_preparation', (adjusted_phase - 0.92) / 0.05
        else:
            return 'foot_placement', (adjusted_phase - 0.97) / 0.03

    def smooth_interp(self, p, vals):
        if p <= 0: return vals[0]
        if p >= 1: return vals[1]
        return vals[0] + (vals[1] - vals[0]) * (3*p**2 - 2*p**3)

    def get_joint_angles(self, phase_name, phase_progress, leg):
        angle_params = {
            'initial_contact': {'thigh': [-0.1, -0.3], 'shank': [0.05, 0.2], 'foot': [-0.2, 0.1]},
            'loading_response': {'thigh': [-0.3, 0.1], 'shank': [0.2, -0.2], 'foot': [0.1, 0.2]},
            'mid_stance': {'thigh': [0.1, 0.4], 'shank': [-0.2, -0.4], 'foot': [0.2, 0.3]},
            'terminal_stance': {'thigh': [0.4, 0.2], 'shank': [-0.4, 0.2], 'foot': [0.3, 0.6]},
            'pre_swing': {'thigh': [0.2, -0.5], 'shank': [0.2, 0.0], 'foot': [0.6, -0.8]},
            'initial_swing': {'thigh': [-0.5, -0.2], 'shank': [0.0, -0.6], 'foot': [-0.8, 0.2]},
            'mid_swing': {'thigh': [-0.2, 0.2], 'shank': [-0.6, 0.0], 'foot': [0.2, -0.2]},
            'terminal_swing': {'thigh': [0.2, -0.1], 'shank': [0.0, 0.1], 'foot': [-0.2, -0.4]},
            'swing_preparation': {'thigh': [-0.1, -0.15], 'shank': [0.1, 0.15], 'foot': [-0.4, -0.3]},
            'foot_placement': {'thigh': [-0.15, -0.1], 'shank': [0.15, 0.05], 'foot': [-0.3, -0.2]}
        }
        params = angle_params[phase_name]
        thigh_angle = self.smooth_interp(phase_progress, params['thigh'])
        shank_angle = self.smooth_interp(phase_progress, params['shank'])
        foot_angle = self.smooth_interp(phase_progress, params['foot'])
        return thigh_angle, shank_angle, foot_angle

    def get_joint_positions(self, time, leg='right'):
        phase_name, phase_progress = self.get_gait_phase_progress(time, leg)
        thigh_angle, shank_angle, foot_angle = self.get_joint_angles(phase_name, phase_progress, leg)

        # --- Mouvement 3D du bassin (simplifié en 2D pour l'instant) ---
        pelvic_tilt = self.pelvic_tilt_amplitude * np.sin(2 * np.pi * self.step_frequency * time)
        pelvic_rotation = self.pelvic_rotation_amplitude * np.sin(2 * np.pi * self.step_frequency * time)
        pelvic_sway = 0.3 * self.pelvic_sway_amplitude * np.sin(2 * np.pi * self.step_frequency * time + np.pi/2) # Réduction du pelvic sway

        hip_x_local = (0.5 if leg == 'right' else -0.4) * pelvic_sway + 0.3 * pelvic_rotation # Ajustement pour la hanche gauche
        hip_y = self.h_hip - pelvic_tilt + 0.1 * pelvic_sway**2

        knee_x_local = hip_x_local + self.l_thigh * np.sin(thigh_angle)
        knee_y = hip_y - self.l_thigh * np.cos(thigh_angle)

        ankle_x_local = knee_x_local + self.l_shank * np.sin(thigh_angle + shank_angle)
        ankle_y = knee_y - self.l_shank * np.cos(thigh_angle + shank_angle)

        foot_start_x_local = ankle_x_local
        foot_start_y = ankle_y
        foot_end_x_local = ankle_x_local + self.l_foot * np.cos(thigh_angle + shank_angle + foot_angle)
        foot_end_y = ankle_y - self.l_foot * np.sin(thigh_angle + shank_angle + foot_angle)

        # --- Gestion du contact au sol améliorée ---
        if phase_name in ['initial_contact', 'loading_response', 'mid_stance', 'terminal_stance', 'pre_swing']:
            if phase_name == 'initial_contact':
                contact_x = self.global_x_position + hip_x_local + ankle_x_local - self.l_foot * np.cos(thigh_angle + shank_angle + foot_angle)
                if leg == 'right':
                    self.contact_x_right = contact_x
                    print(f"Droit - Initial Contact: time={time:.2f}, contact_x_right={self.contact_x_right:.3f}, hip_x_local={hip_x_local:.3f}")
                else:
                    self.contact_x_left = contact_x
                    print(f"Gauche - Initial Contact: time={time:.2f}, contact_x_left={self.contact_x_left:.3f}, hip_x_local={hip_x_local:.3f}")

            alpha_ground = min(1, phase_progress * 10)

            if (leg == 'right' and self.contact_x_right is not None) or (leg == 'left' and self.contact_x_left is not None):
                contact_x_target = self.contact_x_right if leg == 'right' else self.contact_x_left
                target_ankle_x_local = contact_x_target - self.global_x_position - hip_x_local + self.l_foot * np.cos(thigh_angle + shank_angle + foot_angle)
                ankle_x_local = ankle_x_local * (1 - alpha_ground) + target_ankle_x_local * alpha_ground
                target_ankle_y = self.ground_level + np.abs(self.l_foot * np.sin(thigh_angle + shank_angle + foot_angle))
                ankle_y = ankle_y * (1 - alpha_ground) + target_ankle_y * alpha_ground
                foot_start_y = self.ground_level
                foot_end_y = self.ground_level

                knee_x_local = ankle_x_local - self.l_shank * np.sin(thigh_angle + shank_angle)
                knee_y = ankle_y + self.l_shank * np.cos(thigh_angle + shank_angle)
                hip_x_local = knee_x_local - self.l_thigh * np.sin(thigh_angle)
                hip_y = knee_y + self.l_thigh * np.cos(thigh_angle)

                foot_start_x_local = ankle_x_local
                foot_start_y = ankle_y
                foot_end_x_local = ankle_x_local + self.l_foot * np.cos(thigh_angle + shank_angle + foot_angle)
                foot_end_y = ankle_y - self.l_foot * np.sin(thigh_angle + shank_angle + foot_angle)

        elif phase_name in ['initial_swing', 'mid_swing', 'terminal_swing']:
            t_swing = (phase_progress + (0 if leg == 'right' else 0.5)) % 1
            vertical_offset = self.foot_clearance * 4 * t_swing * (1 - t_swing)

            if self.contact_x_right is not None and self.contact_x_left is not None:
                target_x = self.contact_x_left if leg == 'right' else self.contact_x_right
                swing_progress_norm = (phase_progress - 0) / (1)
                horizontal_offset_ankle = (target_x - (self.global_x_position + hip_x_local)) * swing_progress_norm * 0.8
                ankle_x_local = ankle_x_local + horizontal_offset_ankle
                knee_x_local = knee_x_local + horizontal_offset_ankle * 0.3

            ankle_y += vertical_offset * 0.8
            foot_start_x_local = ankle_x_local
            foot_start_y = ankle_y
            foot_end_x_local = ankle_x_local + self.l_foot * np.cos(thigh_angle + shank_angle + foot_angle)
            foot_end_y = ankle_y - self.l_foot * np.sin(thigh_angle + shank_angle + foot_angle)
            knee_y += vertical_offset * 0.3

        return hip_x_local, hip_y, knee_x_local, knee_y, ankle_x_local, ankle_y, foot_start_x_local, foot_start_y, foot_end_x_local, foot_end_y
        

# --- Initialisation de la figure et de l'axe ---
fig, ax = plt.subplots(figsize=(14, 7))
ax.set_xlim(-1, 2)
ax.set_ylim(-0.1, 1.3)
ax.set_aspect('equal')
ax.grid(True, linestyle=':', alpha=0.7)
ax.set_title('Modélisation de la marche humaine', fontsize=14)
ax.set_xlabel('Position horizontale (m)', fontsize=12)
ax.set_ylabel('Position verticale (m)', fontsize=12)

# Ajout d'un sol texturé
ground_x = np.linspace(-10, 10, 100)
ground_y = np.zeros(100)
ax.fill_between(ground_x, ground_y-0.02, ground_y, color='#e6d8ad', alpha=0.5)
ax.plot(ground_x, ground_y, 'k-', lw=1)

# --- Initialisation des éléments graphiques ---
robot = BipedRobot()
line_right, = ax.plot([], [], 'o-', lw=3, color='royalblue', markersize=8, label='Jambe droite')
line_left, = ax.plot([], [], 'o-', lw=3, color='crimson', markersize=8, label='Jambe gauche')
foot_right, = ax.plot([], [], '-', lw=4, color='royalblue')
foot_left, = ax.plot([], [], '-', lw=4, color='crimson')
hip_marker, = ax.plot([], [], 'o', markersize=12, color='black', label='Bassin')
pelvis_line, = ax.plot([], [], '-', lw=2, color='black')
right_foot_support = patches.Rectangle((0,0), 0.1, 0.02, color='blue', alpha=0.3)
left_foot_support = patches.Rectangle((0,0), 0.1, 0.02, color='red', alpha=0.3)
ax.add_patch(right_foot_support)
ax.add_patch(left_foot_support)
ax.legend(loc='upper right', fontsize=10)

# --- Fonction d'animation ---
def animate(i):
    global robot

    time = i / 60
    robot.global_x_position = robot.horizontal_speed * time

    # Calcul du nombre de cycles écoulés
    num_cycles = time / robot.cycle_time
    if num_cycles >= 10:
        return # Arrêter l'animation

    # Calcul des positions
    hx_r, hy_r, kx_r, ky_r, ax_r, ay_r, fsx_r, fsy_r, fex_r, fey_r = robot.get_joint_positions(time, 'right')
    hx_l, hy_l, kx_l, ky_l, ax_l, ay_l, fsx_l, fsy_l, fex_l, fey_l = robot.get_joint_positions(time, 'left')

    # --- Diagnostic pour le bassin ---
    if abs(time - 3.43) < 0.1:
        print(f"DEBUG BASSIN - time={time:.2f}, hx_r={robot.global_x_position + hx_r:.3f}, hx_l={robot.global_x_position + hx_l:.3f}")

    # Mise à jour des segments
    line_right.set_data([robot.global_x_position + hx_r, robot.global_x_position + kx_r, robot.global_x_position + ax_r],
                        [hy_r, ky_r, ay_r])
    foot_right.set_data([robot.global_x_position + fsx_r, robot.global_x_position + fex_r], [fsy_r, fey_r])

    line_left.set_data([robot.global_x_position + hx_l, robot.global_x_position + kx_l, robot.global_x_position + ax_l],
                       [hy_l, ky_l, ay_l])
    foot_left.set_data([robot.global_x_position + fsx_l, robot.global_x_position + fex_l], [fsy_l, fey_l])

    # Mise à jour du bassin
    hip_x_center = robot.global_x_position + (hx_r + hx_l) / 2
    hip_y_center = (hy_r + hy_l) / 2
    hip_marker.set_data([hip_x_center], [hip_y_center])
    pelvis_line.set_data([robot.global_x_position + hx_r, robot.global_x_position + hx_l], [hy_r, hy_l])

    # Mise à jour des zones d'appui
    for patch, contact_x in [(right_foot_support, robot.contact_x_right), (left_foot_support, robot.contact_x_left)]:
        if contact_x is not None:
            patch.set_xy((contact_x - 0.125, robot.ground_level - 0.02))
            patch.set_width(0.25)

    # Recentrage de la vue
    center_x = robot.global_x_position
    ax.set_xlim(center_x - 1.0, center_x + 1.5)

    return line_right, line_left, foot_right, foot_left, hip_marker, pelvis_line, right_foot_support, left_foot_support

# --- Création de l'animation ---
ani = animation.FuncAnimation(
    fig, animate, frames=600, interval=16.67, blit=True
)

plt.tight_layout()
plt.show()