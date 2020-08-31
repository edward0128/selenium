docker exec grid2 start-video

function task()
{
    python3 $task_name
    if [ $? -eq 0 ]; then
        echo "$task_name  PASS" >> report.txt
    else
        echo "$task_name  ERROR" >> report.txt
    fi
}

task_name=SA-0001-1.1.py
task
task_name=SA-0002-1.2.py
task
task_name=SA-0003-2.1.py
task
task_name=SA-0004-2.2.py
task
task_name=SA-0018-2.3.py
task
task_name=SA-0019-2.3.1.py
task
task_name=SA-0020-2.3.3.py
task
task_name=SA-0021-2.3.2.py
task
task_name=SA-0019-2.3.1.py
task
task_name=SA-0024-2.5.py
task
task_name=SA-0025-2.5.1.py
task
task_name=SA-0026-2.5.3.py
task
task_name=SA-0027-2.5.2.py
task
task_name=SA-0025-2.5.1.py
task
task_name=SA-0028-2.5.4.py
task
task_name=SA-0030-2.5.6.py
task
task_name=SA-0035-2.6.1.py
task
task_name=SA-0036-2.6.2.py
task
task_name=SA-0038-2.7.1.py
task
task_name=SA-0039-2.7.2.py
task
docker exec grid2 stop-video
