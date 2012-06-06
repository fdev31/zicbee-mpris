__all__ = ['Player']
import gobject
gobject.threads_init()
from dbus import glib
glib.init_threads()

import mprisremote as MPRIS
import sys

class Player(object):
    _finished = False
    def __init__(self):

        #player_name = os.environ.get('MPRIS_REMOTE_PLAYER', '*')
        player_name = '*'
        self.mpris = MPRIS.MPRISRemote()

        try:
            self.mpris.find_player(player_name)
        except MPRIS.RequestedPlayerNotRunning, e:
            print >>sys.stderr, 'Player "%s" is not running, but the following players were found:' % player_name
            for n in self.mpris.players_running:
                print >>sys.stderr, "    %s" % n.replace("org.mpris.", "")
            print >>sys.stderr, 'If you meant to use one of those players, ' \
                                'set $MPRIS_REMOTE_PLAYER accordingly.'
            raise ValueError("Can't set selected backend")
        except MPRIS.NoPlayersRunning:
            print >>sys.stderr, "No MPRIS-compliant players found running."
            raise RuntimeError("No MPRIS player is running.")


    def set_cache(self, val):
        """ Sets the cache value in kilobytes """
        pass

    def volume(self, val):
        """ Sets volume [0-100] """
        self.mpris.player.VolumeSet(int(val))
        return self.mpris.player.VolumeGet().real

    def seek(self, val):
        """ Seeks specified number of seconds (positive or negative) """
        self.mpris.player.PositionSet(int(val))

    def pause(self):
        """ Toggles pause mode """
        self.mpris.player.Pause()

    def respawn(self):
        """ Restarts the player """
        self.quit()
#        self.mpris.root.Quit()

    def load(self, uri):
        """ Loads the specified URI """
        if uri[0] == '/':
            uri = 'file://'+uri

        try:
            self.mpris.player.Stop()
            for i in range(self.mpris.tracklist.GetLength()):
                self.mpris.tracklist.DelTrack(0)
        except Exception, e:
            print "ERR", repr(e)

        self.mpris.tracklist.AddTrack(uri, True)

    def quit(self):
        """ De-initialize player and wait for it to shut down """
        self.mpris.player.Stop()
        for i in range(self.mpris.tracklist.GetLength()):
            self.mpris.tracklist.DelTrack(0)

    @property
    def position(self):
        """ returns the stream position, in seconds """
        if self.mpris.player.GetStatus()[0].real == 2: # stopped
            return None
        return self.mpris.player.PositionGet().real



if __name__ == '__main__':
    p = Player()
    p.load('http://172.16.41.222:9090/db/get/song.mp3?id=5ZR')
