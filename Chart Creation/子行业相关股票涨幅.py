from iFinDPy import THS_iFinDLogin,THS_HistoryQuotes,THS_Trans2DataFrame,THS_iFinDLogout,THS_EDBQuery,THS_BasicData
from plot_func import *
import pandas as pd
from get_data_func import * 

codes = """000568.SZ
000596.SZ
000639.SZ
000716.SZ
000729.SZ
000752.SZ
000799.SZ
000848.SZ
000858.SZ
000860.SZ
000869.SZ
000895.SZ
000929.SZ
000995.SZ
001215.SZ
002216.SZ
002304.SZ
002329.SZ
002330.SZ
002461.SZ
002481.SZ
002495.SZ
002507.SZ
002515.SZ
002557.SZ
002568.SZ
002570.SZ
002582.SZ
002597.SZ
002646.SZ
002650.SZ
002661.SZ
002695.SZ
002702.SZ
002719.SZ
002726.SZ
002732.SZ
002820.SZ
002840.SZ
002847.SZ
002910.SZ
002946.SZ
002956.SZ
002991.SZ
003000.SZ
003030.SZ
300146.SZ
300741.SZ
300783.SZ
300791.SZ
300858.SZ
300892.SZ
300898.SZ
300908.SZ
300915.SZ
300973.SZ
300997.SZ
600059.SH
600073.SH
600084.SH
600132.SH
600186.SH
600189.SH
600197.SH
600199.SH
600238.SH
600300.SH
600305.SH
600365.SH
600381.SH
600419.SH
600429.SH
600519.SH
600543.SH
600559.SH
600573.SH
600597.SH
600600.SH
600616.SH
600702.SH
600779.SH
600809.SH
600866.SH
600872.SH
600882.SH
600887.SH
601579.SH
603020.SH
603027.SH
603043.SH
603156.SH
603198.SH
603288.SH
603317.SH
603345.SH
603369.SH
603517.SH
603536.SH
603589.SH
603696.SH
603697.SH
603711.SH
603719.SH
603755.SH
603777.SH
603779.SH
603866.SH
603886.SH
603919.SH
605077.SH
605089.SH
605179.SH
605300.SH
605337.SH
605338.SH
605339.SH
605388.SH
605499.SH
688089.SH""".split("\n")
if __name__ == '__main__':
    x,y = get_top_gainers_by_industry(codes,start_date="2023-11-06",end_date="2023-11-10")
    get_bar(x[:8],y[:8],"/home/luzhenye/data/png/test/test.png")
