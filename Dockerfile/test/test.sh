pytest test-all.py  -o log_cli=true -o log_cli_level=INFO --html=report.html --self-contained-html

python3 -m  pytest test-all.py::TestDemotest::test_sa_0001  -o log_cli=true -o log_cli_level=INFO --html=report.html --self-contained-html