from SciQLop.backend import TimeRange
from datetime import datetime

from SciQLopPlots import QCPAxis, QCPColorGradient, QCPAxisTickerLog, QCPRange


# all plots are stacked
p = main_window.new_plot_panel()
p.time_range = TimeRange(
    datetime(2022, 6, 1, 0, 4, 30).timestamp(),
    datetime(2022, 6, 5, 13, 6, 0).timestamp(),
)

plot_names = [
    "brtn",
    "density",
    "V",
    "eflux_vs_energy",
    "eflux_vs_theta",
    "eflux_vs_phi",
]
plots_idx = {plot_name: i for plot_name, i in zip(plot_names, range(len(plot_names)))}

p.plot(
    #    "speasy/cda/ParkerSolarProbe/PSP_FLD/MAG_RTN/PSP_FLD_L2_MAG_RTN/psp_fld_l2_mag_RTN"
    "speasy/cda/ParkerSolarProbe/PSP_FLD/MAG_RTN_1min/PSP_FLD_L2_MAG_RTN_1MIN/psp_fld_l2_mag_RTN_1min"
)

p.plot(
    "speasy/cda/ParkerSolarProbe/PSP_FLD/SQTN_V1V2/PSP_FLD_L3_SQTN_RFS_V1V2/electron_density"
)
p.plots[plots_idx["density"]].plot(
    "speasy/cda/ParkerSolarProbe/PSPSWEAPSPAN/PSP_SWP_SPI_SF00_L3_MOM/DENS"
)


p.plot("speasy/cda/ParkerSolarProbe/PSPSWEAPSPAN/PSP_SWP_SPI_SF00_L3_MOM/VEL_RTN_SUN")

p.plot(
    "speasy/cda/ParkerSolarProbe/PSPSWEAPSPAN/PSP_SWP_SPE_SF0_L3_PAD/EFLUX_VS_ENERGY"
)
#    "speasy/cda/ParkerSolarProbe/PSPSWEAPSPAN/PSP_SWP_SPI_SF00_L3_MOM/EFLUX_VS_ENERGY"


p.plot(
    "speasy/cda/ParkerSolarProbe/PSPSWEAPSPAN/PSP_SWP_SPI_SF00_L3_MOM/EFLUX_VS_ENERGY"
)

p.plot("speasy/cda/ParkerSolarProbe/PSPSWEAPSPAN/PSP_SWP_SPI_SF00_L3_MOM/EFLUX_VS_PHI")


p.plots[plots_idx["brtn"]].yAxis.setRange(-1200, 1200)
p.plots[plots_idx["density"]].yAxis.setRange(1.0, 5000)
p.plots[plots_idx["density"]].yAxis.setScaleType(QCPAxis.stLogarithmic)
p.plots[plots_idx["density"]].yAxis.setTicker(QCPAxisTickerLog())
p.plots[plots_idx["V"]].yAxis.setRange(-600, 1100)


for plot in p.plots:
    plot.replot()
