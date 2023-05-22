#!/usr/bin/bash

cd /home/kali/Practice/htb
session="htb-ts"

tmux new-session -d -s $session -n 'main'
tmux split-window -h
tmux split-window -v -p 33
tmux send-keys "tty-clock" Enter
tmux new-window -d -t '=htb-ts' -n 'second'
tmux select-window -t $session:1
tmux split-window -h
tmux new-window -d -t '=htb-ts' -n 'openvpn'
tmux select-window -t $session:2
tmux select-window -t $session:0
tmux select-pane -t 0
tmux attach
