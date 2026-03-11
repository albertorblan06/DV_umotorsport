# UM-Driverless Project Structure

This document provides a high-level overview of the repository structure to help agents quickly navigate the workspace. Auto-generated via Python.

```
umotorsport/
├── .agents/
│   ├── errors.md
│   └── metodology.md
├── TODO.md
├── kart_brain/
│   ├── .agents/
│   │   ├── README.md
│   │   ├── architecture.md
│   │   ├── error_log.md
│   │   ├── orin_environment.md
│   │   ├── orin_flash_guide.md
│   │   ├── postmortems/
│   │   │   └── README.md
│   │   ├── scratchpad.md
│   │   ├── simulation.md
│   │   └── vm_environment.md
│   ├── .gitignore
│   ├── .gitmodules
│   ├── AGENTS.md
│   ├── CLAUDE.md
│   ├── README.md
│   ├── TODO.md
│   ├── docs/
│   │   ├── ACTUATION_PROTOCOL.md
│   │   └── PROJECT_VISION.md
│   ├── models/
│   │   └── perception/
│   │       └── yolo/
│   ├── proto/
│   │   ├── generate.sh
│   │   ├── generated_c/
│   │   │   ├── kart_msgs.pb.c
│   │   │   └── kart_msgs.pb.h
│   │   ├── kart_msgs.proto
│   │   └── nanopb/
│   │       └── kart_msgs.options
│   ├── pyproject.toml
│   ├── run_live.sh
│   ├── run_live_3d.sh
│   ├── scripts/
│   │   ├── fix_output_limit.sh
│   │   ├── install_deps.sh
│   │   ├── patch_test_main.py
│   │   ├── run_yolo_on_media.py
│   │   ├── sim2d/
│   │   │   ├── __init__.py
│   │   │   ├── controllers.py
│   │   │   ├── ga.py
│   │   │   ├── generate_sdf.py
│   │   │   ├── kart_model.py
│   │   │   ├── perception.py
│   │   │   ├── results/
│   │   │   ├── results_autocross_v5/
│   │   │   ├── results_cma_v2_best.json
│   │   │   ├── results_cma_v2_noisy_best.json
│   │   │   ├── results_cma_v3_finetuned_best.json
│   │   │   ├── results_v3/
│   │   │   ├── results_v3b/
│   │   │   ├── results_v4_fresh/
│   │   │   ├── sim.py
│   │   │   ├── track.py
│   │   │   ├── train.py
│   │   │   └── visualize.py
│   │   └── sine_steering_test.py
│   ├── src/
│   │   ├── TODO.md
│   │   ├── ThirdParty/
│   │   │   ├── rviz-plugin-zed-od/
│   │   │   ├── test-bus-can/
│   │   │   ├── zed-ros2-wrapper/
│   │   │   └── zed_display_rviz2/
│   │   ├── joy_to_cmd_vel/
│   │   │   ├── CMakeLists.txt
│   │   │   ├── package.xml
│   │   │   └── src/
│   │   ├── kart_bringup/
│   │   │   ├── CMakeLists.txt
│   │   │   ├── config/
│   │   │   ├── launch/
│   │   │   ├── package.xml
│   │   │   └── scripts/
│   │   ├── kart_perception/
│   │   │   ├── kart_perception/
│   │   │   ├── launch/
│   │   │   ├── package.xml
│   │   │   ├── resource/
│   │   │   ├── setup.cfg
│   │   │   └── setup.py
│   │   ├── kart_sim/
│   │   │   ├── CMakeLists.txt
│   │   │   ├── config/
│   │   │   ├── launch/
│   │   │   ├── models/
│   │   │   ├── package.xml
│   │   │   ├── scripts/
│   │   │   └── worlds/
│   │   ├── kb_coms_micro/
│   │   │   ├── CMakeLists.txt
│   │   │   ├── include/
│   │   │   ├── package.xml
│   │   │   └── src/
│   │   ├── kb_dashboard/
│   │   │   ├── kb_dashboard/
│   │   │   ├── launch/
│   │   │   ├── package.xml
│   │   │   ├── resource/
│   │   │   ├── setup.cfg
│   │   │   ├── setup.py
│   │   │   └── test/
│   │   ├── kb_interfaces/
│   │   │   ├── CMakeLists.txt
│   │   │   ├── msg/
│   │   │   └── package.xml
│   │   └── kb_serial_driver_lib/
│   │       ├── CMakeLists.txt
│   │       ├── include/
│   │       └── src/
│   ├── stuff.md
│   ├── test_data/
│   │   └── driverless_test_media/
│   │       ├── cone_0.png
│   │       ├── cone_1.png
│   │       ├── cone_10.png
│   │       ├── cone_11.png
│   │       ├── cone_12.png
│   │       ├── cone_13.png
│   │       ├── cone_14.png
│   │       ├── cone_2.png
│   │       ├── cone_3.png
│   │       ├── cone_4.png
│   │       ├── cone_5.png
│   │       ├── cone_6.png
│   │       ├── cone_7.png
│   │       ├── cone_8.png
│   │       ├── cone_9.png
│   │       ├── cones_image.png
│   │       ├── cones_test.png
│   │       ├── image1.png
│   │       ├── image2.jpg
│   │       ├── image3.webp
│   │       ├── meme1.jpg
│   │       ├── meme2.jpg
│   │       ├── video.mp4
│   │       ├── video_short.mp4
│   │       └── videosim.mp4
│   └── training/
│       ├── README.md
│       └── perception/
│           ├── dataset.yaml
│           ├── prepare_dataset.py
│           ├── pyproject.toml
│           ├── sources.yaml
│           └── train.py
├── kart_docs/
│   ├── .gitignore
│   ├── .python-version
│   ├── CLAUDE.md
│   ├── GEMINI.md
│   ├── LICENSE
│   ├── README.md
│   ├── TODO.md
│   ├── dev.sh
│   ├── docs/
│   │   ├── assembly/
│   │   │   ├── electronics/
│   │   │   ├── emergency-braking/
│   │   │   ├── index.md
│   │   │   ├── powertrain/
│   │   │   ├── sensors/
│   │   │   └── steering/
│   │   ├── assets/
│   │   │   └── datasheets/
│   │   ├── bom/
│   │   │   └── index.md
│   │   ├── contact.md
│   │   ├── faq.md
│   │   ├── hydraulics/
│   │   │   ├── index/
│   │   │   └── index.md
│   │   ├── index.md
│   │   ├── software/
│   │   │   └── index.md
│   │   └── tools/
│   │       ├── index.md
│   │       └── tools.yaml
│   ├── generate_bom_hook.py
│   ├── generate_bom_reports.sh
│   ├── generate_llm_files.py
│   ├── generate_llm_hook.py
│   ├── install.sh
│   ├── mkdocs.yml
│   ├── pyproject.toml
│   ├── scripts/
│   │   └── aggregate_bom.py
│   ├── stuff/
│   │   └── install_in_windows.md
│   ├── stuff.md
│   ├── test-docs.sh
│   └── uv.lock
├── kart_medulla/
│   ├── .agents/
│   │   └── settings.local.json
│   ├── .gitignore
│   ├── AGENTS.md
│   ├── CMakeLists.txt
│   ├── Doxyfile
│   ├── README.md
│   ├── TODO.md
│   ├── components/
│   │   ├── bluepad32/
│   │   │   ├── CMakeLists.txt
│   │   │   ├── Kconfig
│   │   │   ├── arch/
│   │   │   ├── bt/
│   │   │   ├── controller/
│   │   │   ├── idf_component.yml
│   │   │   ├── include/
│   │   │   ├── parser/
│   │   │   ├── platform/
│   │   │   ├── uni_circular_buffer.c
│   │   │   ├── uni_gpio.c
│   │   │   ├── uni_hid_device.c
│   │   │   ├── uni_init.c
│   │   │   ├── uni_joystick.c
│   │   │   ├── uni_log.c
│   │   │   ├── uni_mouse_quadrature.c
│   │   │   ├── uni_property.c
│   │   │   ├── uni_utils.c
│   │   │   ├── uni_version.c
│   │   │   └── uni_virtual_device.c
│   │   ├── btstack/
│   │   │   ├── 3rd-party/
│   │   │   ├── CMakeLists.txt
│   │   │   ├── Kconfig
│   │   │   ├── Kconfig.projbuild
│   │   │   ├── btstack_audio_esp32_v4.c
│   │   │   ├── btstack_audio_esp32_v5.c
│   │   │   ├── btstack_port_esp32.c
│   │   │   ├── btstack_stdio_esp32.c
│   │   │   ├── btstack_tlv_esp32.c
│   │   │   ├── es8388.c
│   │   │   ├── es8388.h
│   │   │   ├── include/
│   │   │   ├── platform/
│   │   │   ├── src/
│   │   │   └── tool/
│   │   ├── cmd_nvs/
│   │   │   ├── CMakeLists.txt
│   │   │   ├── cmd_nvs.c
│   │   │   ├── cmd_nvs.h
│   │   │   └── component.mk
│   │   ├── cmd_nvs_4.4/
│   │   │   ├── CMakeLists.txt
│   │   │   ├── cmd_nvs.c
│   │   │   ├── cmd_nvs.h
│   │   │   └── component.mk
│   │   ├── cmd_system/
│   │   │   ├── CMakeLists.txt
│   │   │   ├── cmd_system.c
│   │   │   ├── cmd_system.h
│   │   │   └── component.mk
│   │   ├── cmd_system_4.4/
│   │   │   ├── CMakeLists.txt
│   │   │   ├── cmd_system.c
│   │   │   ├── cmd_system.h
│   │   │   └── component.mk
│   │   ├── km_act/
│   │   │   ├── CMakeLists.txt
│   │   │   ├── km_act.c
│   │   │   └── km_act.h
│   │   ├── km_coms/
│   │   │   ├── CMakeLists.txt
│   │   │   ├── km_coms.c
│   │   │   └── km_coms.h
│   │   ├── km_gamc/
│   │   │   ├── CMakeLists.txt
│   │   │   ├── km_gamc.c
│   │   │   └── km_gamc.h
│   │   ├── km_gpio/
│   │   │   ├── CMakeLists.txt
│   │   │   ├── km_gpio.c
│   │   │   └── km_gpio.h
│   │   ├── km_objects/
│   │   │   ├── CMakeLists.txt
│   │   │   ├── km_objects.c
│   │   │   └── km_objects.h
│   │   ├── km_pid/
│   │   │   ├── CMakeLists.txt
│   │   │   ├── km_pid.c
│   │   │   └── km_pid.h
│   │   ├── km_proto/
│   │   │   ├── CMakeLists.txt
│   │   │   ├── kart_msgs.pb.c
│   │   │   └── kart_msgs.pb.h
│   │   ├── km_rtos/
│   │   │   ├── CMakeLists.txt
│   │   │   ├── km_rtos.c
│   │   │   └── km_rtos.h
│   │   ├── km_sdir/
│   │   │   ├── CMakeLists.txt
│   │   │   ├── km_sdir.c
│   │   │   └── km_sdir.h
│   │   ├── km_sta/
│   │   │   ├── CMakeLists.txt
│   │   │   ├── km_sta.c
│   │   │   └── km_sta.h
│   │   └── nanopb/
│   │       ├── CMakeLists.txt
│   │       ├── pb.h
│   │       ├── pb_common.c
│   │       ├── pb_common.h
│   │       ├── pb_decode.c
│   │       ├── pb_decode.h
│   │       ├── pb_encode.c
│   │       └── pb_encode.h
│   ├── controller_gui.py
│   ├── dependencies.lock
│   ├── docs/
│   │   ├── html/
│   │   │   └── [Truncated generated doc files...]
│   │   └── latex/
│   │   │   └── [Truncated generated doc files...]
│   │       ├── Makefile
│   │       ├── annotated.tex
│   │       ├── dir_0be146286b66fbe11f5f7fdb27e840f2.tex
│   │       ├── dir_0be146286b66fbe11f5f7fdb27e840f2_dep.md5
│   │       ├── dir_0be146286b66fbe11f5f7fdb27e840f2_dep.pdf
│   │       ├── dir_0cbba8142cf066dfd3279b94fe217756.tex
│   │       ├── dir_0cbba8142cf066dfd3279b94fe217756_dep.md5
│   │       ├── dir_0cbba8142cf066dfd3279b94fe217756_dep.pdf
│   │       ├── dir_409f97388efe006bc3438b95e9edef48.tex
│   │       ├── dir_409f97388efe006bc3438b95e9edef48_dep.md5
│   │       ├── dir_409f97388efe006bc3438b95e9edef48_dep.pdf
│   │       ├── dir_42bdd7633a74fafd2decd6d67f2f678f.tex
│   │       ├── dir_42bdd7633a74fafd2decd6d67f2f678f_dep.md5
│   │       ├── dir_42bdd7633a74fafd2decd6d67f2f678f_dep.pdf
│   │       ├── dir_5c982d53a68cdbcd421152b4020263a9.tex
│   │       ├── dir_5c982d53a68cdbcd421152b4020263a9_dep.md5
│   │       ├── dir_5c982d53a68cdbcd421152b4020263a9_dep.pdf
│   │       ├── dir_7114e0ac5d1498e823632cfbc539dd73.tex
│   │       ├── dir_7114e0ac5d1498e823632cfbc539dd73_dep.md5
│   │       ├── dir_7114e0ac5d1498e823632cfbc539dd73_dep.pdf
│   │       ├── dir_8ef7473ceafd51bb4da56169dd128df0.tex
│   │       ├── dir_8ef7473ceafd51bb4da56169dd128df0_dep.md5
│   │       ├── dir_8ef7473ceafd51bb4da56169dd128df0_dep.pdf
│   │       ├── dir_90d6d11a4ccba9ad35ecc2163c33d9dd.tex
│   │       ├── dir_90d6d11a4ccba9ad35ecc2163c33d9dd_dep.md5
│   │       ├── dir_90d6d11a4ccba9ad35ecc2163c33d9dd_dep.pdf
│   │       ├── dir_b4b868a43e708476a6479b402415828e.tex
│   │       ├── dir_b4b868a43e708476a6479b402415828e_dep.md5
│   │       ├── dir_b4b868a43e708476a6479b402415828e_dep.pdf
│   │       ├── dir_f91a524d88148dcb2278cbce6649cd3a.tex
│   │       ├── dir_f91a524d88148dcb2278cbce6649cd3a_dep.md5
│   │       ├── dir_f91a524d88148dcb2278cbce6649cd3a_dep.pdf
│   │       ├── doxygen.sty
│   │       ├── etoc_doxygen.sty
│   │       ├── files.tex
│   │       ├── km__coms_8c.tex
│   │       ├── km__coms_8c__incl.md5
│   │       ├── km__coms_8c__incl.pdf
│   │       ├── km__coms_8c_source.tex
│   │       ├── km__coms_8h.tex
│   │       ├── km__coms_8h__dep__incl.md5
│   │       ├── km__coms_8h__dep__incl.pdf
│   │       ├── km__coms_8h__incl.md5
│   │       ├── km__coms_8h__incl.pdf
│   │       ├── km__coms_8h_source.tex
│   │       ├── km__gamc_8c.tex
│   │       ├── km__gamc_8c__incl.md5
│   │       ├── km__gamc_8c__incl.pdf
│   │       ├── km__gamc_8c_source.tex
│   │       ├── km__gamc_8h.tex
│   │       ├── km__gamc_8h__dep__incl.md5
│   │       ├── km__gamc_8h__dep__incl.pdf
│   │       ├── km__gamc_8h__incl.md5
│   │       ├── km__gamc_8h__incl.pdf
│   │       ├── km__gamc_8h_source.tex
│   │       ├── km__gpio_8c.tex
│   │       ├── km__gpio_8c__incl.md5
│   │       ├── km__gpio_8c__incl.pdf
│   │       ├── km__gpio_8c_source.tex
│   │       ├── km__gpio_8h.tex
│   │       ├── km__gpio_8h__dep__incl.md5
│   │       ├── km__gpio_8h__dep__incl.pdf
│   │       ├── km__gpio_8h__incl.md5
│   │       ├── km__gpio_8h__incl.pdf
│   │       ├── km__gpio_8h_source.tex
│   │       ├── km__objects_8c.tex
│   │       ├── km__objects_8c__incl.md5
│   │       ├── km__objects_8c__incl.pdf
│   │       ├── km__objects_8c_source.tex
│   │       ├── km__objects_8h.tex
│   │       ├── km__objects_8h__dep__incl.md5
│   │       ├── km__objects_8h__dep__incl.pdf
│   │       ├── km__objects_8h__incl.md5
│   │       ├── km__objects_8h__incl.pdf
│   │       ├── km__objects_8h_source.tex
│   │       ├── km__pid_8c.tex
│   │       ├── km__pid_8c__incl.md5
│   │       ├── km__pid_8c__incl.pdf
│   │       ├── km__pid_8c_source.tex
│   │       ├── km__pid_8h.tex
│   │       ├── km__pid_8h__dep__incl.md5
│   │       ├── km__pid_8h__dep__incl.pdf
│   │       ├── km__pid_8h__incl.md5
│   │       ├── km__pid_8h__incl.pdf
│   │       ├── km__pid_8h_source.tex
│   │       ├── km__rtos_8c.tex
│   │       ├── km__rtos_8c__incl.md5
│   │       ├── km__rtos_8c__incl.pdf
│   │       ├── km__rtos_8c_source.tex
│   │       ├── km__rtos_8h.tex
│   │       ├── km__rtos_8h__dep__incl.md5
│   │       ├── km__rtos_8h__dep__incl.pdf
│   │       ├── km__rtos_8h__incl.md5
│   │       ├── km__rtos_8h__incl.pdf
│   │       ├── km__rtos_8h_source.tex
│   │       ├── km__sdir_8c.tex
│   │       ├── km__sdir_8c__incl.md5
│   │       ├── km__sdir_8c__incl.pdf
│   │       ├── km__sdir_8c_source.tex
│   │       ├── km__sdir_8h.tex
│   │       ├── km__sdir_8h__dep__incl.md5
│   │       ├── km__sdir_8h__dep__incl.pdf
│   │       ├── km__sdir_8h__incl.md5
│   │       ├── km__sdir_8h__incl.pdf
│   │       ├── km__sdir_8h_source.tex
│   │       ├── km__sta_8c.tex
│   │       ├── km__sta_8c__incl.md5
│   │       ├── km__sta_8c__incl.pdf
│   │       ├── km__sta_8c_source.tex
│   │       ├── km__sta_8h.tex
│   │       ├── km__sta_8h__dep__incl.md5
│   │       ├── km__sta_8h__dep__incl.pdf
│   │       ├── km__sta_8h__incl.md5
│   │       ├── km__sta_8h__incl.pdf
│   │       ├── km__sta_8h_source.tex
│   │       ├── longtable_doxygen.sty
│   │       ├── main_8c.tex
│   │       ├── main_8c__incl.md5
│   │       ├── main_8c__incl.pdf
│   │       ├── main_8c_source.tex
│   │       ├── refman.aux
│   │       ├── refman.idx
│   │       ├── refman.ilg
│   │       ├── refman.ind
│   │       ├── refman.log
│   │       ├── refman.out
│   │       ├── refman.pdf
│   │       ├── refman.tex
│   │       ├── refman.toc
│   │       ├── structPID__Controller.tex
│   │       ├── structRTOS__Task.tex
│   │       ├── structkm__coms__msg.tex
│   │       ├── structsensor__struct.tex
│   │       └── tabu_doxygen.sty
│   ├── flash_test.sh
│   ├── include/
│   │   └── README
│   ├── lib/
│   │   └── README
│   ├── main/
│   │   ├── CMakeLists.txt
│   │   ├── cal_main.c
│   │   ├── main.c
│   │   ├── main_backup.c
│   │   ├── main_normal.c
│   │   ├── main_test_a.c
│   │   ├── main_test_b.c
│   │   ├── main_test_c.c
│   │   ├── main_test_d.c
│   │   ├── sketch.cpp
│   │   └── test_main.c
│   ├── monitor_serial.py
│   ├── patches/
│   │   └── 0001-Call-initBluepad32-when-AUTOSTART_ARDUINO-is-enabled.patch
│   ├── platformio.ini
│   ├── sdkconfig
│   ├── sdkconfig.defaults
│   ├── sdkconfig.esp32-c3-devkitc-02
│   ├── sdkconfig.esp32-c6-devkitc-1
│   ├── sdkconfig.esp32-s3-devkitc-1
│   ├── sdkconfig.old
│   ├── stuff/
│   │   ├── ESP32-pinout-diagram.jpg
│   │   └── MD30C Users Manual.pdf
│   └── test/
│       └── README
└── project_vision.md
```
