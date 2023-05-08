#!/bin/sh

set -e

# shellcheck disable=SC2046
. $(poetry env info --path)/bin/activate

exec app migrate -- upgrade head && app server
