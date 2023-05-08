#!/bin/sh
###
 # @Software: Visual Studio Code
 # @Author: StudentCWZ
 # @Email: StudentCWZ@outlook.com
 # @Date: 2023-05-08 14:25:30
 # @Last Modified by: StudentCWZ
 # @Description:
###
set -e

# shellcheck disable=SC2046
. $(poetry env info --path)/bin/activate

exec app server
