# -*- coding: utf-8 -*-
from __future__ import print_function

import os
import stat
import sys

# find the import for catkin's python package - either from source space or from an installed underlay
if os.path.exists(os.path.join('/opt/ros/melodic/share/catkin/cmake', 'catkinConfig.cmake.in')):
    sys.path.insert(0, os.path.join('/opt/ros/melodic/share/catkin/cmake', '..', 'python'))
try:
    from catkin.environment_cache import generate_environment_script
except ImportError:
    # search for catkin package in all workspaces and prepend to path
    for workspace in '/home/kailin/ros/autoware.ai/install/ymc;/home/kailin/ros/autoware.ai/install/xsens_driver;/home/kailin/ros/autoware.ai/install/wf_simulator;/home/kailin/ros/autoware.ai/install/lattice_planner;/home/kailin/ros/autoware.ai/install/waypoint_planner;/home/kailin/ros/autoware.ai/install/waypoint_maker;/home/kailin/ros/autoware.ai/install/way_planner;/home/kailin/ros/autoware.ai/install/vlg22c_cam;/home/kailin/ros/autoware.ai/install/vision_ssd_detect;/home/kailin/ros/autoware.ai/install/vision_segment_enet_detect;/home/kailin/ros/autoware.ai/install/vision_lane_detect;/home/kailin/ros/autoware.ai/install/vision_darknet_detect;/home/kailin/ros/autoware.ai/install/vision_beyond_track;/home/kailin/ros/autoware.ai/install/vel_pose_diff_checker;/home/kailin/ros/autoware.ai/install/vehicle_model;/home/kailin/ros/autoware.ai/install/vehicle_gazebo_simulation_launcher;/home/kailin/ros/autoware.ai/install/vehicle_gazebo_simulation_interface;/home/kailin/ros/autoware.ai/install/vehicle_description;/home/kailin/ros/autoware.ai/install/trafficlight_recognizer;/home/kailin/ros/autoware.ai/install/op_utilities;/home/kailin/ros/autoware.ai/install/op_simulation_package;/home/kailin/ros/autoware.ai/install/op_local_planner;/home/kailin/ros/autoware.ai/install/op_global_planner;/home/kailin/ros/autoware.ai/install/lidar_kf_contour_track;/home/kailin/ros/autoware.ai/install/op_ros_helpers;/home/kailin/ros/autoware.ai/install/ff_waypoint_follower;/home/kailin/ros/autoware.ai/install/dp_planner;/home/kailin/ros/autoware.ai/install/op_simu;/home/kailin/ros/autoware.ai/install/op_planner;/home/kailin/ros/autoware.ai/install/op_utility;/home/kailin/ros/autoware.ai/install/lidar_euclidean_cluster_detect;/home/kailin/ros/autoware.ai/install/vector_map_server;/home/kailin/ros/autoware.ai/install/road_occupancy_processor;/home/kailin/ros/autoware.ai/install/costmap_generator;/home/kailin/ros/autoware.ai/install/object_map;/home/kailin/ros/autoware.ai/install/naive_motion_predict;/home/kailin/ros/autoware.ai/install/map_file;/home/kailin/ros/autoware.ai/install/libvectormap;/home/kailin/ros/autoware.ai/install/lane_planner;/home/kailin/ros/autoware.ai/install/imm_ukf_pda_track;/home/kailin/ros/autoware.ai/install/decision_maker;/home/kailin/ros/autoware.ai/install/vector_map;/home/kailin/ros/autoware.ai/install/vector_map_msgs;/home/kailin/ros/autoware.ai/install/vectacam;/home/kailin/ros/autoware.ai/install/twist_generator;/home/kailin/ros/autoware.ai/install/twist_gate;/home/kailin/ros/autoware.ai/install/twist_filter;/home/kailin/ros/autoware.ai/install/twist2odom;/home/kailin/ros/autoware.ai/install/tablet_socket_msgs;/home/kailin/ros/autoware.ai/install/state_machine_lib;/home/kailin/ros/autoware.ai/install/sound_player;/home/kailin/ros/autoware.ai/install/sick_lms5xx;/home/kailin/ros/autoware.ai/install/sick_ldmrs_tools;/home/kailin/ros/autoware.ai/install/sick_ldmrs_driver;/home/kailin/ros/autoware.ai/install/sick_ldmrs_msgs;/home/kailin/ros/autoware.ai/install/sick_ldmrs_description;/home/kailin/ros/autoware.ai/install/points2image;/home/kailin/ros/autoware.ai/install/rosinterface;/home/kailin/ros/autoware.ai/install/rosbag_controller;/home/kailin/ros/autoware.ai/install/pure_pursuit;/home/kailin/ros/autoware.ai/install/points_preprocessor;/home/kailin/ros/autoware.ai/install/mpc_follower;/home/kailin/ros/autoware.ai/install/lidar_localizer;/home/kailin/ros/autoware.ai/install/emergency_handler;/home/kailin/ros/autoware.ai/install/autoware_health_checker;/home/kailin/ros/autoware.ai/install/as;/home/kailin/ros/autoware.ai/install/ros_observer;/home/kailin/ros/autoware.ai/install/roi_object_filter;/home/kailin/ros/autoware.ai/install/range_vision_fusion;/home/kailin/ros/autoware.ai/install/qpoases_vendor;/home/kailin/ros/autoware.ai/install/pos_db;/home/kailin/ros/autoware.ai/install/points_downsampler;/home/kailin/ros/autoware.ai/install/pixel_cloud_fusion;/home/kailin/ros/autoware.ai/install/pcl_omp_registration;/home/kailin/ros/autoware.ai/install/pc2_downsampler;/home/kailin/ros/autoware.ai/install/oculus_socket;/home/kailin/ros/autoware.ai/install/obj_db;/home/kailin/ros/autoware.ai/install/nmea_navsat;/home/kailin/ros/autoware.ai/install/ndt_tku;/home/kailin/ros/autoware.ai/install/ndt_cpu;/home/kailin/ros/autoware.ai/install/mrt_cmake_modules;/home/kailin/ros/autoware.ai/install/microstrain_driver;/home/kailin/ros/autoware.ai/install/memsic_imu;/home/kailin/ros/autoware.ai/install/marker_downsampler;/home/kailin/ros/autoware.ai/install/lidar_shape_estimation;/home/kailin/ros/autoware.ai/install/lidar_point_pillars;/home/kailin/ros/autoware.ai/install/lidar_naive_l_shape_detect;/home/kailin/ros/autoware.ai/install/lidar_fake_perception;/home/kailin/ros/autoware.ai/install/lidar_apollo_cnn_seg_detect;/home/kailin/ros/autoware.ai/install/libwaypoint_follower;/home/kailin/ros/autoware.ai/install/lgsvl_simulator_bridge;/home/kailin/ros/autoware.ai/install/lanelet2_extension;/home/kailin/ros/autoware.ai/install/lanelet2_validation;/home/kailin/ros/autoware.ai/install/lanelet2_examples;/home/kailin/ros/autoware.ai/install/lanelet2_python;/home/kailin/ros/autoware.ai/install/lanelet2_routing;/home/kailin/ros/autoware.ai/install/lanelet2_traffic_rules;/home/kailin/ros/autoware.ai/install/lanelet2_projection;/home/kailin/ros/autoware.ai/install/lanelet2_maps;/home/kailin/ros/autoware.ai/install/lanelet2_io;/home/kailin/ros/autoware.ai/install/lanelet2_core;/home/kailin/ros/autoware.ai/install/kvaser;/home/kailin/ros/autoware.ai/install/kitti_player;/home/kailin/ros/autoware.ai/install/kitti_box_publisher;/home/kailin/ros/autoware.ai/install/javad_navsat_driver;/home/kailin/ros/autoware.ai/install/integrated_viewer;/home/kailin/ros/autoware.ai/install/image_processor;/home/kailin/ros/autoware.ai/install/hokuyo;/home/kailin/ros/autoware.ai/install/graph_tools;/home/kailin/ros/autoware.ai/install/gnss_localizer;/home/kailin/ros/autoware.ai/install/gnss;/home/kailin/ros/autoware.ai/install/glviewer;/home/kailin/ros/autoware.ai/install/gazebo_world_description;/home/kailin/ros/autoware.ai/install/gazebo_imu_description;/home/kailin/ros/autoware.ai/install/gazebo_camera_description;/home/kailin/ros/autoware.ai/install/garmin;/home/kailin/ros/autoware.ai/install/freespace_planner;/home/kailin/ros/autoware.ai/install/fastvirtualscan;/home/kailin/ros/autoware.ai/install/ekf_localizer;/home/kailin/ros/autoware.ai/install/ds4_msgs;/home/kailin/ros/autoware.ai/install/ds4_driver;/home/kailin/ros/autoware.ai/install/detected_objects_visualizer;/home/kailin/ros/autoware.ai/install/decision_maker_panel;/home/kailin/ros/autoware.ai/install/data_preprocessor;/home/kailin/ros/autoware.ai/install/custom_msgs;/home/kailin/ros/autoware.ai/install/calibration_publisher;/home/kailin/ros/autoware.ai/install/autoware_system_msgs;/home/kailin/ros/autoware.ai/install/autoware_rviz_plugins;/home/kailin/ros/autoware.ai/install/autoware_quickstart_examples;/home/kailin/ros/autoware.ai/install/autoware_pointgrey_drivers;/home/kailin/ros/autoware.ai/install/autoware_driveworks_interface;/home/kailin/ros/autoware.ai/install/autoware_connector;/home/kailin/ros/autoware.ai/install/astar_search;/home/kailin/ros/autoware.ai/install/amathutils_lib;/home/kailin/ros/autoware.ai/install/autoware_msgs;/home/kailin/ros/autoware.ai/install/autoware_map_msgs;/home/kailin/ros/autoware.ai/install/autoware_launcher_rviz;/home/kailin/ros/autoware.ai/install/autoware_launcher;/home/kailin/ros/autoware.ai/install/autoware_lanelet2_msgs;/home/kailin/ros/autoware.ai/install/autoware_external_msgs;/home/kailin/ros/autoware.ai/install/autoware_driveworks_gmsl_interface;/home/kailin/ros/autoware.ai/install/autoware_config_msgs;/home/kailin/ros/autoware.ai/install/autoware_can_msgs;/home/kailin/ros/autoware.ai/install/autoware_build_flags;/home/kailin/ros/autoware.ai/install/autoware_bag_tools;/home/kailin/ros/autoware.ai/install/adi_driver;/opt/ros/melodic'.split(';'):
        python_path = os.path.join(workspace, 'lib/python2.7/dist-packages')
        if os.path.isdir(os.path.join(python_path, 'catkin')):
            sys.path.insert(0, python_path)
            break
    from catkin.environment_cache import generate_environment_script

code = generate_environment_script('/home/kailin/ros/motion_planning_for_mobile_robots_ROS/hw_1/catkin_ws/src/cmake-build-debug/devel/env.sh')

output_filename = '/home/kailin/ros/motion_planning_for_mobile_robots_ROS/hw_1/catkin_ws/src/cmake-build-debug/catkin_generated/setup_cached.sh'
with open(output_filename, 'w') as f:
    # print('Generate script for cached setup "%s"' % output_filename)
    f.write('\n'.join(code))

mode = os.stat(output_filename).st_mode
os.chmod(output_filename, mode | stat.S_IXUSR)
