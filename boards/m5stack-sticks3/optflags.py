# Make -O2 effective on this env.
#
# The Arduino framework for ESP32-S3 appends "-Os -ffunction-sections
# -fdata-sections" to CCFLAGS AFTER every user build_flag (see
# framework-arduinoespressif32-libs/esp32s3/pioarduino-build.py), and gcc uses
# the LAST -O option, so a plain "-O2" in build_flags is silently overridden.
# This post script strips the framework "-Os" and appends "-O2" so the
# optimization level actually applies to the app + libraries.

Import("env")

ccflags = list(env.get("CCFLAGS", []))
env["CCFLAGS"] = [f for f in ccflags if f != "-Os"]
env.Append(CCFLAGS=["-O2"])
