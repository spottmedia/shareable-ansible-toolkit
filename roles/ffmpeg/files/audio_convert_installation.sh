#!/bin/bash

mkdir ~/ffmpeg_sources
#cd ~/ffmpeg_sources
#wget http://www.tortall.net/projects/yasm/releases/yasm-1.3.0.tar.gz
#tar xzvf yasm-1.3.0.tar.gz
#cd yasm-1.3.0
#./configure --prefix="$HOME/ffmpeg_build" --bindir="/usr/bin"
#make
#make install
#make distclean
#
#cd ~/ffmpeg_sources
#wget -O fdk-aac.zip https://github.com/mstorsjo/fdk-aac/zipball/master
#unzip fdk-aac.zip
#cd mstorsjo-fdk-aac*
#autoreconf -fiv
#./configure --prefix="$HOME/ffmpeg_build" --disable-shared
#make
#make install
#make distclean

cd ~/ffmpeg_sources
wget http://ffmpeg.org/releases/ffmpeg-snapshot.tar.bz2
tar xjvf ffmpeg-snapshot.tar.bz2
#sudo chown -R vagrant ffmpeg
#sudo chgrp -R vagrant ffmpeg
#sudo chmod -R 777 ffmpeg
cd ffmpeg
#PATH="$PATH:$HOME/bin" ./configure \
#  --prefix="$HOME/ffmpeg_build" \
#  --extra-cflags="-I$HOME/ffmpeg_build/include" \
#  --extra-ldflags="-L$HOME/ffmpeg_build/lib" \
#  --bindir="$HOME/bin" \
#  --enable-gpl \
#  --enable-libfdk-aac \
#  --enable-libfreetype \
#  --enable-libvorbis \
#  --enable-libmp3lame \
#  --enable-nonfree
#PATH="$PATH:$HOME/bin" make
#make install
#make distclean
#hash -r

hg clone https://bitbucket.org/multicoreware/x265
cd x265/build/linux
PATH="$HOME/bin:$PATH" cmake -G "Unix Makefiles" -DCMAKE_INSTALL_PREFIX="$HOME/ffmpeg_build" -DENABLE_SHARED:bool=off ../../source && PATH="$HOME/bin:$PATH"
make
make install

PATH="$HOME/bin:$PATH" PKG_CONFIG_PATH="$HOME/ffmpeg_build/lib/pkgconfig" \
   ./configure \
  --prefix="$HOME/ffmpeg_build" \
  --pkg-config-flags="--static" \
  --extra-cflags="-I$HOME/ffmpeg_build/include" \
  --extra-ldflags="-L$HOME/ffmpeg_build/lib" \
  --extra-libs="-lpthread -lm" \
  --bindir="$HOME/bin" \
  --enable-gpl \
  --enable-libass \
  --enable-libfdk-aac \
  --enable-libfreetype \
  --enable-libmp3lame \
  --enable-libopus \
  --enable-libtheora \
  --enable-libvorbis \
  --enable-libvpx \
  --enable-libx264 \
  --enable-libx265 \
  --enable-nonfree && \
PATH="$HOME/bin:$PATH" make && make install

#Move the bin folder to /var/www and change the owners
mkdir -p /var/www/bin
cd ~/bin
cp * /var/www/bin