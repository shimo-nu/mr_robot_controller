import launch
import os
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, ExecuteProcess, SetLaunchConfiguration
from launch.substitutions import LaunchConfiguration, Command, ThisLaunchFileDir
from launch.conditions import IfCondition
from launch_ros.actions import Node

from ament_index_python.packages import get_package_share_directory

def generate_launch_description():
    mr_robot_converter_share_dir = get_package_share_directory('mr_robot_converter')
    config_file_path = os.path.join(mr_robot_converter_share_dir, 'config', 'bridge_config.yaml')
    print(config_file_path)
    return LaunchDescription([
        # 宣言: config, from_domain, to_domain
        DeclareLaunchArgument(
            'config',
            default_value=config_file_path,
            description='Path to YAML configuration'
        ),
      
        Node(
            package='domain_bridge',
            executable='domain_bridge',
            arguments=[
                LaunchConfiguration('config')
            ],
            output='both'
        )
    ])
