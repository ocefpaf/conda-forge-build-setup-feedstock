conda config --add channels conda-forge
conda config --set show_channel_urls true
conda config --set add_pip_as_python_dependency false

if test `uname` = "Linux"
then
  # 2 cores are available on CircleCI workers: https://discuss.circleci.com/t/what-runs-on-the-node-container-by-default/1443
  # MAKEFLAGS is passed through conda build: https://github.com/conda/conda-build/pull/917
  export MAKEFLAGS="-j2 ${MAKEFLAGS}"
fi
