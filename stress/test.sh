# export HOST_NUM="1"
# python3 -m  pytest test-all.py::TestDemotest::test_create_site  -o log_cli=true -o log_cli_level=INFO --html=./log/report$HOST_NUM.html --self-contained-html &
# export HOST_NUM="2"
# python3 -m  pytest test-all.py::TestDemotest::test_create_site  -o log_cli=true -o log_cli_level=INFO --html=./log/report$HOST_NUM.html --self-contained-html &
# export HOST_NUM="3"
# python3 -m  pytest test-all.py::TestDemotest::test_create_site  -o log_cli=true -o log_cli_level=INFO --html=./log/report$HOST_NUM.html --self-contained-html &
# export HOST_NUM="4"
# python3 -m  pytest test-all.py::TestDemotest::test_create_site  -o log_cli=true -o log_cli_level=INFO --html=./log/report$HOST_NUM.html --self-contained-html &
# export HOST_NUM="5"
# python3 -m  pytest test-all.py::TestDemotest::test_create_site  -o log_cli=true -o log_cli_level=INFO --html=./log/report$HOST_NUM.html --self-contained-html &

for i in {1..3}
do
    export HOST_NUM=$i
    python3 -m  pytest test-all.py::TestDemotest::test_create_site  -o log_cli=true -o log_cli_level=INFO --html=./log/report$i.html --self-contained-html &
    sleep 1
done
