docker exec -it alicevision_conan_client_1 bash


git clone https://github.com/EstebanDugueperoux2/conan-center-index.git
cd conan-center-index/recipes/opencascade/all/
git switch feature/AddNewOCCTRelease
conan create . --version 7.8.1 --build missing -c tools.system.package_manager:mode=install 

git clone https://github.com/EstebanDugueperoux2/IfcOpenShell.git
cd IfcOpenShell/
git switch feature/AddConanSupport
conan create . -s build_type=Debug --profile:build .conan/profiles/build_profile --profile:host .conan/profiles/build_profile -c tools.system.package_manager:mode=install --build missing &> build.log

conan create . -s build_type=Debug -o */*:shared=True --profile:build .conan/profiles/build_profile --profile:host .conan/profiles/build_profile -c tools.system.package_manager:mode=install --build missing &> build_shared.log

