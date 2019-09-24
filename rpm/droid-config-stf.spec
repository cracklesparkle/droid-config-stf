# These and other macros are documented in
# ../droid-configs-device/droid-configs.inc
%define device stf
%define vendor honor
%define vendor_pretty Honor
%define vendor_pretty 9
%define dcd_path ./
# Adjust this for your device
%define pixel_ratio 2.0
# We assume most devices will
%define have_modem 1
%include droid-configs-device/droid-configs.inc
