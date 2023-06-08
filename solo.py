from SciQLop.backend import TimeRange
from datetime import datetime

from SciQLopPlots import QCPAxis, QCPColorGradient, QCPAxisTickerLog, QCPRange


# all plots are stacked
p = main_window.new_plot_panel()
p.time_range = TimeRange(
    datetime(2021, 7, 21, 0, 4, 30).timestamp(),
    datetime(2021, 7, 21, 23, 6, 0).timestamp(),
)

plot_names = [
    "density",
    "B",
    "Vr",
    "Vtn",
    "eflux",
]
plots_idx = {plot_name: i for plot_name, i in zip(plot_names, range(len(plot_names)))}

p.plot("speasy/cda/Solar_Orbiter/SOLO/SWA_PAS/SOLO_L2_SWA_PAS_GRND_MOM/N")
p.plot("speasy/cda/Solar_Orbiter/SOLO/MAG/SOLO_L2_MAG_RTN_NORMAL/B_RTN")
p.plot("speasy/cda/Solar_Orbiter/SOLO/SWA_PAS/SOLO_L2_SWA_PAS_GRND_MOM/V_RTN")
p.plot("speasy/cda/Solar_Orbiter/SOLO/SWA_PAS/SOLO_L2_SWA_PAS_GRND_MOM/V_RTN")
p.plot("speasy/cda/Solar_Orbiter/SOLO/SWA_PAS/SOLO_L2_SWA_PAS_EFLUX/eflux")


p.plots[plots_idx["density"]].yAxis.setRange(1, 20)
p.plots[plots_idx["B"]].yAxis.setRange(-10, 10)
p.plots[plots_idx["Vr"]].yAxis.setRange(350, 500)
p.plots[plots_idx["Vtn"]].yAxis.setRange(-60, 60)
# p.plots[plots_idx["density"]].yAxis.setScaleType(QCPAxis.stLogarithmic)
# p.plots[plots_idx["density"]].yAxis.setTicker(QCPAxisTickerLog())


for plot in p.plots:
    plot.replot()
