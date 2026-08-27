@echo off
REM 创建并激活 Python 虚拟环境（Windows）

IF NOT EXIST .venv (
    python -m venv .venv
)

echo.
echo 激活虚拟环境（PowerShell）:
echo     .\.venv\Scripts\activate
echo.
echo 激活虚拟环境（CMD）:
echo     .venv\Scripts\activate.bat
echo.
echo 创建完成，请手动激活并安装依赖：
echo     pip install numpy scipy sympy pandas matplotlib seaborn networkx statsmodels scikit-learn
