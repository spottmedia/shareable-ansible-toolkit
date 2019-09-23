mkdir ~/ffmpeg_sources
cd ~/ffmpeg_sources
wget http://www.tortall.net/projects/yasm/releases/yasm-1.3.0.tar.gz
tar xzvf yasm-1.3.0.tar.gz
cd yasm-1.3.0
./configure --prefix="$HOME/ffmpeg_build" --bindir="$HOME/bin"
make
make install
make distclean

cd ~/ffmpeg_sources
wget -O fdk-aac.zip https://github.com/mstorsjo/fdk-aac/zipball/master
unzip fdk-aac.zip
cd mstorsjo-fdk-aac*
autoreconf -fiv
./configure --prefix="$HOME/ffmpeg_build" --disable-shared
make
make install
make distclean

cd ~/ffmpeg_sources
wget http://ffmpeg.org/releases/ffmpeg-snapshot.tar.bz2
tar xjvf ffmpeg-snapshot.tar.bz2
sudo chown -R vagrant ffmpeg
sudo chgrp -R vagrant ffmpeg
sudo chmod -R 777 ffmpeg
cd ffmpeg
PATH="$PATH:$HOME/bin" ./configure \
  --prefix="$HOME/ffmpeg_build" \
  --extra-cflags="-I$HOME/ffmpeg_build/include" \
  --extra-ldflags="-L$HOME/ffmpeg_build/lib" \
  --bindir="$HOME/bin" \
  --enable-gpl \
  --enable-libfdk-aac \
  --enable-libfreetype \
  --enable-libvorbis \
  --enable-libmp3lame \
  --enable-nonfree
PATH="$PATH:$HOME/bin" make
make install
make distclean
hash -r

#Move the bin folder to /var/www and change the owners
mkdir -p /var/www/bin
cd ~/bin
cp * /var/www/bin