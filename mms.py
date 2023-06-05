from SciQLop.backend import TimeRange
from datetime import datetime

from SciQLopPlots import QCPAxis, QCPColorGradient, QCPAxisTickerLog, QCPRange


# all plots are stacked
p = main_window.new_plot_panel()
p.time_range = TimeRange(
    datetime(2018, 12, 5, 10, 4, 30).timestamp(),
    datetime(2018, 12, 5, 16, 6, 0).timestamp(),
)

plot_names = ["spectro_fast", "spectro_brst", "V", "fgm", "tB", "n"]
plots_idx = {plot_name: i for plot_name, i in zip(plot_names, range(len(plot_names)))}

p.plot(
    "speasy/cda/MMS/MMS1/DIS/MMS1_FPI_FAST_L2_DIS_MOMS/mms1_dis_energyspectr_omni_fast"
)
p.plot(
    "speasy/cda/MMS/MMS1/DIS/MMS1_FPI_BRST_L2_DIS_MOMS/mms1_dis_energyspectr_omni_brst"
)

p.plot("speasy/cda/MMS/MMS1/DIS/MMS1_FPI_FAST_L2_DIS_MOMS/mms1_dis_bulkv_gse_fast")
p.plots[plots_idx["V"]].plot(
    "speasy/cda/MMS/MMS1/DIS/MMS1_FPI_BRST_L2_DIS_MOMS/mms1_dis_bulkv_gse_brst"
)
p.plot("speasy/cda/MMS/MMS1/FGM/MMS1_FGM_SRVY_L2/mms1_fgm_b_gsm_srvy_l2")

p.plot("speasy/cda/MMS/MMS1/DIS/MMS1_FPI_FAST_L2_DIS_MOMS/mms1_dis_temppara_fast")
p.plots[plots_idx["tB"]].plot(
    "speasy/cda/MMS/MMS1/DIS/MMS1_FPI_FAST_L2_DIS_MOMS/mms1_dis_tempperp_fast"
)
p.plot("speasy/cda/MMS/MMS1/DIS/MMS1_FPI_FAST_L2_DIS_MOMS/mms1_dis_numberdensity_fast")

p.plots[plots_idx["n"]].plot(
    "speasy/cda/MMS/MMS1/DIS/MMS1_FPI_BRST_L2_DIS_MOMS/mms1_dis_numberdensity_brst"
)


p.plots[plots_idx["tB"]].yAxis.setRange(180, 1500)
p.plots[plots_idx["fgm"]].yAxis.setRange(-75, 75)
p.plots[plots_idx["n"]].yAxis.setRange(0.001, 50)
p.plots[plots_idx["V"]].yAxis.setRange(-450, 450)
p.plots[plots_idx["tB"]].yAxis.setScaleType(QCPAxis.stLogarithmic)
p.plots[plots_idx["n"]].yAxis.setScaleType(QCPAxis.stLogarithmic)
p.plots[plots_idx["tB"]].yAxis.setTicker(QCPAxisTickerLog())
p.plots[plots_idx["n"]].yAxis.setTicker(QCPAxisTickerLog())


for plot in p.plots:
    plot.replot()
