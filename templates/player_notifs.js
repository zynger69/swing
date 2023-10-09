if ('mediaSession' in navigator) {
  navigator.mediaSession.metadata = new MediaMetadata({
    title: '{{ songs.name }}',
    artist: '{{ songs.desc|safe }}'.replaceAll("&",","),
    {% if songs.alb.name != "Swing" %}
      album : '{{ songs.alb.name }}',
    {% endif %}
    artwork: [
      { src: '{{ songs.spic }}' },
    ]
  });

  navigator.mediaSession.setActionHandler('previoustrack', () => {
    playPrev();
  });
  
  navigator.mediaSession.setActionHandler('nexttrack', () => {
    playNext();
  });
  
  navigator.mediaSession.setActionHandler('play', () => {
    Play();
  });
  
  navigator.mediaSession.setActionHandler('pause', () => {
    Pause();
  });
  

 // seekto
  navigator.mediaSession.setActionHandler('seekto', (details) => {
    if (details.fastSeek && 'fastSeek' in audio) {
      audio.fastSeek(details.seekTime);
      return;
    }
    audio.currentTime = details.seekTime;
  });
  
  //backward
  navigator.mediaSession.setActionHandler('seekbackward', (details) => {
    audio.currentTime = audio.currentTime - (details.seekOffset || 10);
  });
  
  //forward
  navigator.mediaSession.setActionHandler('seekforward', (details) => {
    audio.currentTime = audio.currentTime + (details.seekOffset || 10);
  });

}




