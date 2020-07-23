set -ex

# if local build, exit
if [ -z "${CODEBUILD_BUILD_IMAGE}" ]; then
  exit 0
fi

# upload files
DISTRIBUTION="el7"
RELEASE_DIRS="dev"
# if production release, add prod
if [ ! -z "${PROD_RELEASE}" ]; then
  RELEASE_DIRS="${RELEASE_DIRS} prod"
fi
for RELEASE_DIR in $RELEASE_DIRS; do
  for DIR in RPMS SRPMS SPECS SOURCES; do
    aws s3 cp --recursive ./${DIR}/ s3://${S3REPOBUCKET}/${RELEASE_DIR}/${DISTRIBUTION}/${DIR}/
  done
done
