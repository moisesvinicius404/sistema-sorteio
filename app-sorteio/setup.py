from cx_Freeze import setup, Executable

# Dependências adicionais, se necessário
build_exe_options = {
    "packages": [],
    "excludes": [],
    "include_files": ["dice.png"],  # Adicione aqui os arquivos adicionais necessários
}

# Configuração do setup
setup(
    name="SorteioApp",
    version="0.1",
    description="Sistema de Sorteio",
    options={"build_exe": build_exe_options},
    executables=[Executable("sorteio.py", base=None)],
)
