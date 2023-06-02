from SciQLop.backend import TimeRange
from datetime import datetime

from SciQLopPlots import QCPAxis, QCPColorGradient, QCPAxisTickerLog, QCPRange

# all plots are stacked
p = main_window.new_plot_panel()
p.time_range = TimeRange(
    datetime(2009, 12, 5, 0, 14, 30).timestamp(),
    datetime(2009, 12, 6, 0, 18, 0).timestamp(),
)

# Spectro ions
p.plot("speasy/cda/THEMIS/THA/L2/THA_L2_ESA/tha_peif_en_eflux")

# Bulk ion speed GSE
p.plot("speasy/cda/THEMIS/THA/L2/THA_L2_MOM/tha_peim_velocity_gsm")
p.plots[1].plot(
    "speasy/cda/THEMIS/THA/L2/THA_L2_ESA/tha_peir_t3speasy/cda/THEMIS/THA/L2/THA_L2_ESA/tha_peib_velocity_gse"
)  # burst

# Tempréature ions
p.plot("speasy/cda/THEMIS/THA/L2/THA_L2_ESA/tha_peir_magt3")
p.plots[2].plot("speasy/cda/THEMIS/THA/L2/THA_L2_MOM/tha_peim_t3_mag")

# Champ magnétique GSM
p.plot("speasy/cda/THEMIS/THA/L2/THA_L2_FGM/tha_fgh_gsm")
p.plots[3].plot("speasy/cda/THEMIS/THA/L2/THA_L2_FGM/tha_fgs_gsm")


# Density ions
p.plot("speasy/cda/THEMIS/THA/L2/THA_L2_ESA/tha_peir_density")
p.plots[4].plot("speasy/cda/THEMIS/THA/L2/THA_L2_ESA/tha_peib_density")  # burst


p.plots[2].yAxis.setRange(10, 2000)
p.plots[3].yAxis.setRange(-75, 75)
p.plots[4].yAxis.setRange(0.01, 150)
p.plots[1].yAxis.setRange(-450, 450)
p.plots[4].yAxis.setScaleType(QCPAxis.stLogarithmic)
p.plots[2].yAxis.setScaleType(QCPAxis.stLogarithmic)

for plot in p.plots:
    plot.replot()
