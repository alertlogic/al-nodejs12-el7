set -ex
BUILD_DIR=$PWD
TAG=$(git describe --tags --long)
PKGVERSION=$(echo $TAG | cut -d '-' -f1)
PKGRELEASE=$(echo $TAG | cut -d '-' -f2)

# clean rpm build environment
rm -rf ${BUILD_DIR}/BUILD/*
rm -rf ${BUILD_DIR}/BUILDROOT/*
rm -rf ${BUILD_DIR}/RPMS/*
rm -rf ${BUILD_DIR}/SRPMS/*

# build rpm
rpmbuild \
    --define "_topdir ${BUILD_DIR}"\
    -D "version ${PKGVERSION}"\
    -D "release ${PKGRELEASE}"\
    -ba ${BUILD_DIR}/SPECS/al-nodejs12-el7.spec
