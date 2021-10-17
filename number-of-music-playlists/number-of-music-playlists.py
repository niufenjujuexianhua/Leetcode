class Solution(object):
    def numMusicPlaylists(self, N, L, K):
        """
        :type n: int
        :type goal: int
        :type k: int
        :rtype: int
        """
        MOD = 10**9+7
        seen = {}
        def dp(unique_songs, listened_songs):
            if unique_songs == 0 and listened_songs==0:return 1
            if unique_songs<0 or unique_songs>listened_songs:return 0
            if (unique_songs, listened_songs) in seen:
                return seen[(unique_songs, listened_songs)]
            
            res = dp(unique_songs-1, listened_songs-1)*(N-(unique_songs-1))  % MOD
            if unique_songs-K > 0:
                res += dp(unique_songs, listened_songs-1)*(unique_songs-K) % MOD
            
            seen[(unique_songs, listened_songs)] = res % MOD
            return res % MOD
        return dp(N, L)