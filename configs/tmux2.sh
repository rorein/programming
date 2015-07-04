# Mount /dev/sda2 if it's not mounted
if [ ! -d "$HOME/Data/Jeff" ]; then
  sudo mount -t ntfs /dev/sda2 "$HOME/Data"
  xdg-user-dirs-update
fi

tmux
