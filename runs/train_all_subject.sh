python main.py --summary --all_subject --model=bci2021 --band=0,4,4,7,7,13,13,30,30,42 --labels=0,1 --start_time=-0.5 --end_time=4 --window_size=400 --step=50 -lr=1e-04 -sch=exp --gamma=0.993 --epochs=400 --batch_size=144 --save_dir=train --device=0