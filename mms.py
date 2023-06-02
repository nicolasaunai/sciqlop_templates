from SciQLop.backend import TimeRange
from datetime import datetime

from SciQLopPlots import QCPAxis, QCPColorGradient, QCPAxisTickerLog, QCPRange


# all plots are stacked
p = main_window.new_plot_panel()
p.time_range = TimeRange(
    datetime(2018, 12, 5, 10, 4, 30).timestamp(),
    datetime(2018, 12, 5, 16, 6, 0).timestamp(),
)
p.plot(
    "speasy/cda/MMS/MMS1/DIS/MMS1_FPI_FAST_L2_DIS_MOMS/mms1_dis_energyspectr_omni_fast"
)
p.plot("speasy/cda/MMS/MMS1/DIS/MMS1_FPI_FAST_L2_DIS_MOMS/mms1_dis_temppara_fast")
p.plots[1].plot(
    "speasy/cda/MMS/MMS1/DIS/MMS1_FPI_FAST_L2_DIS_MOMS/mms1_dis_tempperp_fast"
)
p.plot("speasy/cda/MMS/MMS1/FGM/MMS1_FGM_SRVY_L2/mms1_fgm_b_gsm_srvy_l2")
p.plot("speasy/cda/MMS/MMS1/DIS/MMS1_FPI_FAST_L2_DIS_MOMS/mms1_dis_numberdensity_fast")
p.plot("speasy/cda/MMS/MMS1/DIS/MMS1_FPI_FAST_L2_DIS_MOMS/mms1_dis_bulkv_gse_fast")
p.plots[4].plot(
    "speasy/cda/MMS/MMS1/DIS/MMS1_FPI_BRST_L2_DIS_MOMS/mms1_dis_bulkv_gse_brst"
)
p.plots[3].plot(
    "speasy/cda/MMS/MMS1/DIS/MMS1_FPI_BRST_L2_DIS_MOMS/mms1_dis_numberdensity_brst"
)


p.plots[1].yAxis.setRange(180, 1500)
p.plots[2].yAxis.setRange(-75, 75)
p.plots[3].yAxis.setRange(0.001, 50)
p.plots[4].yAxis.setRange(-450, 450)
p.plots[1].yAxis.setScaleType(QCPAxis.stLogarithmic)
p.plots[3].yAxis.setScaleType(QCPAxis.stLogarithmic)


for plot in p.plots:
    plot.replot()
