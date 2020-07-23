set -ex
BUILD_DIR=$PWD

# clean rpm build environment
rm -rf ${BUILD_DIR}/BUILD/*
rm -rf ${BUILD_DIR}/BUILDROOT/*
rm -rf ${BUILD_DIR}/RPMS/*
rm -rf ${BUILD_DIR}/SRPMS/*
