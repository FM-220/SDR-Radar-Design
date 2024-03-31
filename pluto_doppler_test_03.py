#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#
# SPDX-License-Identifier: GPL-3.0
#
# GNU Radio Python Flow Graph
# Title: Not titled yet
# GNU Radio version: 3.9.7.0

from distutils.version import StrictVersion

if __name__ == '__main__':
    import ctypes
    import sys
    if sys.platform.startswith('linux'):
        try:
            x11 = ctypes.cdll.LoadLibrary('libX11.so')
            x11.XInitThreads()
        except:
            print("Warning: failed to XInitThreads()")

from PyQt5 import Qt
from gnuradio import qtgui
from gnuradio.filter import firdes
import sip
from gnuradio import analog
from gnuradio import blocks
from gnuradio import filter
from gnuradio import gr
from gnuradio.fft import window
import sys
import signal
from argparse import ArgumentParser
from gnuradio.eng_arg import eng_float, intx
from gnuradio import eng_notation
from gnuradio import soapy
from gnuradio.qtgui import Range, RangeWidget
from PyQt5 import QtCore
import pluto_doppler_test_03_epy_block_0 as epy_block_0  # embedded python block



from gnuradio import qtgui

class pluto_doppler_test_03(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "Not titled yet", catch_exceptions=True)
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Not titled yet")
        qtgui.util.check_set_qss()
        try:
            self.setWindowIcon(Qt.QIcon.fromTheme('gnuradio-grc'))
        except:
            pass
        self.top_scroll_layout = Qt.QVBoxLayout()
        self.setLayout(self.top_scroll_layout)
        self.top_scroll = Qt.QScrollArea()
        self.top_scroll.setFrameStyle(Qt.QFrame.NoFrame)
        self.top_scroll_layout.addWidget(self.top_scroll)
        self.top_scroll.setWidgetResizable(True)
        self.top_widget = Qt.QWidget()
        self.top_scroll.setWidget(self.top_widget)
        self.top_layout = Qt.QVBoxLayout(self.top_widget)
        self.top_grid_layout = Qt.QGridLayout()
        self.top_layout.addLayout(self.top_grid_layout)

        self.settings = Qt.QSettings("GNU Radio", "pluto_doppler_test_03")

        try:
            if StrictVersion(Qt.qVersion()) < StrictVersion("5.0.0"):
                self.restoreGeometry(self.settings.value("geometry").toByteArray())
            else:
                self.restoreGeometry(self.settings.value("geometry"))
        except:
            pass

        ##################################################
        # Variables
        ##################################################
        self.tx_gain = tx_gain = 40
        self.tone_freq = tone_freq = 500
        self.samp_rate = samp_rate = 2400000
        self.rx_gain = rx_gain = 40
        self.rx_deci = rx_deci = 50
        self.doppler_gain = doppler_gain = 40

        ##################################################
        # Blocks
        ##################################################
        self._tx_gain_range = Range(0, 89, 1, 40, 200)
        self._tx_gain_win = RangeWidget(self._tx_gain_range, self.set_tx_gain, "'tx_gain'", "counter_slider", float, QtCore.Qt.Horizontal)
        self.top_grid_layout.addWidget(self._tx_gain_win, 0, 0, 1, 1)
        for r in range(0, 1):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(0, 1):
            self.top_grid_layout.setColumnStretch(c, 1)
        self.soapy_plutosdr_source_0 = None
        dev = 'driver=plutosdr'
        stream_args = ''
        tune_args = ['']
        settings = ['']

        self.soapy_plutosdr_source_0 = soapy.source(dev, "fc32", 1, '',
                                  stream_args, tune_args, settings)
        self.soapy_plutosdr_source_0.set_sample_rate(0, samp_rate)
        self.soapy_plutosdr_source_0.set_bandwidth(0, 0.0)
        self.soapy_plutosdr_source_0.set_gain_mode(0, False)
        self.soapy_plutosdr_source_0.set_frequency(0, 3.5e9)
        self.soapy_plutosdr_source_0.set_gain(0, min(max(50, 0.0), 73.0))
        self.soapy_plutosdr_sink_0 = None
        dev = 'driver=plutosdr'
        stream_args = ''
        tune_args = ['']
        settings = ['']

        self.soapy_plutosdr_sink_0 = soapy.sink(dev, "fc32", 1, '',
                                  stream_args, tune_args, settings)
        self.soapy_plutosdr_sink_0.set_sample_rate(0, samp_rate)
        self.soapy_plutosdr_sink_0.set_bandwidth(0, 0.0)
        self.soapy_plutosdr_sink_0.set_frequency(0, 3.5e9)
        self.soapy_plutosdr_sink_0.set_gain(0, min(max(tx_gain, 0.0), 89.0))
        self._rx_gain_range = Range(0, 73, 1, 40, 200)
        self._rx_gain_win = RangeWidget(self._rx_gain_range, self.set_rx_gain, "'rx_gain'", "counter_slider", float, QtCore.Qt.Horizontal)
        self.top_grid_layout.addWidget(self._rx_gain_win, 0, 1, 1, 1)
        for r in range(0, 1):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(1, 2):
            self.top_grid_layout.setColumnStretch(c, 1)
        self.qtgui_number_sink_0 = qtgui.number_sink(
            gr.sizeof_float,
            0,
            qtgui.NUM_GRAPH_VERT,
            1,
            None # parent
        )
        self.qtgui_number_sink_0.set_update_time(0.10)
        self.qtgui_number_sink_0.set_title("")

        labels = ['', '', '', '', '',
            '', '', '', '', '']
        units = ['', '', '', '', '',
            '', '', '', '', '']
        colors = [("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"),
            ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black")]
        factor = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]

        for i in range(1):
            self.qtgui_number_sink_0.set_min(i, -1)
            self.qtgui_number_sink_0.set_max(i, 100)
            self.qtgui_number_sink_0.set_color(i, colors[i][0], colors[i][1])
            if len(labels[i]) == 0:
                self.qtgui_number_sink_0.set_label(i, "Data {0}".format(i))
            else:
                self.qtgui_number_sink_0.set_label(i, labels[i])
            self.qtgui_number_sink_0.set_unit(i, units[i])
            self.qtgui_number_sink_0.set_factor(i, factor[i])

        self.qtgui_number_sink_0.enable_autoscale(True)
        self._qtgui_number_sink_0_win = sip.wrapinstance(self.qtgui_number_sink_0.qwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_number_sink_0_win)
        self.qtgui_freq_sink_x_0_0_0 = qtgui.freq_sink_c(
            32768, #size
            window.WIN_FLATTOP, #wintype
            0, #fc
            samp_rate/rx_deci, #bw
            "", #name
            1,
            None # parent
        )
        self.qtgui_freq_sink_x_0_0_0.set_update_time(0.10)
        self.qtgui_freq_sink_x_0_0_0.set_y_axis(-140, 10)
        self.qtgui_freq_sink_x_0_0_0.set_y_label('Relative Gain', 'dB')
        self.qtgui_freq_sink_x_0_0_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, 0.0, 0, "")
        self.qtgui_freq_sink_x_0_0_0.enable_autoscale(False)
        self.qtgui_freq_sink_x_0_0_0.enable_grid(False)
        self.qtgui_freq_sink_x_0_0_0.set_fft_average(1.0)
        self.qtgui_freq_sink_x_0_0_0.enable_axis_labels(True)
        self.qtgui_freq_sink_x_0_0_0.enable_control_panel(True)
        self.qtgui_freq_sink_x_0_0_0.set_fft_window_normalized(False)



        labels = ['', '', '', '', '',
            '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
            "magenta", "yellow", "dark red", "dark green", "dark blue"]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
            1.0, 1.0, 1.0, 1.0, 1.0]

        for i in range(1):
            if len(labels[i]) == 0:
                self.qtgui_freq_sink_x_0_0_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_freq_sink_x_0_0_0.set_line_label(i, labels[i])
            self.qtgui_freq_sink_x_0_0_0.set_line_width(i, widths[i])
            self.qtgui_freq_sink_x_0_0_0.set_line_color(i, colors[i])
            self.qtgui_freq_sink_x_0_0_0.set_line_alpha(i, alphas[i])

        self._qtgui_freq_sink_x_0_0_0_win = sip.wrapinstance(self.qtgui_freq_sink_x_0_0_0.qwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_freq_sink_x_0_0_0_win)
        self.low_pass_filter_0 = filter.fir_filter_ccf(
            50,
            firdes.low_pass(
                1,
                samp_rate,
                800,
                250,
                window.WIN_HAMMING,
                6.76))
        self.epy_block_0 = epy_block_0.doppler_velocity_calc(transmitted_freq=500, speed_of_light=300000000.0, samp_rate=2400000, fft_size=32768)
        self._doppler_gain_range = Range(0, 100, 1, 40, 200)
        self._doppler_gain_win = RangeWidget(self._doppler_gain_range, self.set_doppler_gain, "'doppler_gain'", "counter_slider", float, QtCore.Qt.Horizontal)
        self.top_layout.addWidget(self._doppler_gain_win)
        self.blocks_throttle_0 = blocks.throttle(gr.sizeof_gr_complex*1, samp_rate,True)
        self.band_reject_filter_0 = filter.fir_filter_ccf(
            1,
            firdes.band_reject(
                1,
                samp_rate/rx_deci,
                tone_freq-5,
                tone_freq+5,
                5,
                window.WIN_HAMMING,
                6.76))
        self.analog_sig_source_x_0 = analog.sig_source_c(samp_rate, analog.GR_COS_WAVE, tone_freq, 1, 0, 0)


        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_sig_source_x_0, 0), (self.epy_block_0, 1))
        self.connect((self.analog_sig_source_x_0, 0), (self.soapy_plutosdr_sink_0, 0))
        self.connect((self.band_reject_filter_0, 0), (self.epy_block_0, 0))
        self.connect((self.band_reject_filter_0, 0), (self.qtgui_freq_sink_x_0_0_0, 0))
        self.connect((self.blocks_throttle_0, 0), (self.low_pass_filter_0, 0))
        self.connect((self.epy_block_0, 0), (self.qtgui_number_sink_0, 0))
        self.connect((self.low_pass_filter_0, 0), (self.band_reject_filter_0, 0))
        self.connect((self.soapy_plutosdr_source_0, 0), (self.blocks_throttle_0, 0))


    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "pluto_doppler_test_03")
        self.settings.setValue("geometry", self.saveGeometry())
        self.stop()
        self.wait()

        event.accept()

    def get_tx_gain(self):
        return self.tx_gain

    def set_tx_gain(self, tx_gain):
        self.tx_gain = tx_gain
        self.soapy_plutosdr_sink_0.set_gain(0, min(max(self.tx_gain, 0.0), 89.0))

    def get_tone_freq(self):
        return self.tone_freq

    def set_tone_freq(self, tone_freq):
        self.tone_freq = tone_freq
        self.analog_sig_source_x_0.set_frequency(self.tone_freq)
        self.band_reject_filter_0.set_taps(firdes.band_reject(1, self.samp_rate/self.rx_deci, self.tone_freq-5, self.tone_freq+5, 5, window.WIN_HAMMING, 6.76))

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.analog_sig_source_x_0.set_sampling_freq(self.samp_rate)
        self.band_reject_filter_0.set_taps(firdes.band_reject(1, self.samp_rate/self.rx_deci, self.tone_freq-5, self.tone_freq+5, 5, window.WIN_HAMMING, 6.76))
        self.blocks_throttle_0.set_sample_rate(self.samp_rate)
        self.low_pass_filter_0.set_taps(firdes.low_pass(1, self.samp_rate, 800, 250, window.WIN_HAMMING, 6.76))
        self.qtgui_freq_sink_x_0_0_0.set_frequency_range(0, self.samp_rate/self.rx_deci)
        self.soapy_plutosdr_sink_0.set_sample_rate(0, self.samp_rate)
        self.soapy_plutosdr_source_0.set_sample_rate(0, self.samp_rate)

    def get_rx_gain(self):
        return self.rx_gain

    def set_rx_gain(self, rx_gain):
        self.rx_gain = rx_gain

    def get_rx_deci(self):
        return self.rx_deci

    def set_rx_deci(self, rx_deci):
        self.rx_deci = rx_deci
        self.band_reject_filter_0.set_taps(firdes.band_reject(1, self.samp_rate/self.rx_deci, self.tone_freq-5, self.tone_freq+5, 5, window.WIN_HAMMING, 6.76))
        self.qtgui_freq_sink_x_0_0_0.set_frequency_range(0, self.samp_rate/self.rx_deci)

    def get_doppler_gain(self):
        return self.doppler_gain

    def set_doppler_gain(self, doppler_gain):
        self.doppler_gain = doppler_gain




def main(top_block_cls=pluto_doppler_test_03, options=None):

    if StrictVersion("4.5.0") <= StrictVersion(Qt.qVersion()) < StrictVersion("5.0.0"):
        style = gr.prefs().get_string('qtgui', 'style', 'raster')
        Qt.QApplication.setGraphicsSystem(style)
    qapp = Qt.QApplication(sys.argv)

    tb = top_block_cls()

    tb.start()

    tb.show()

    def sig_handler(sig=None, frame=None):
        tb.stop()
        tb.wait()

        Qt.QApplication.quit()

    signal.signal(signal.SIGINT, sig_handler)
    signal.signal(signal.SIGTERM, sig_handler)

    timer = Qt.QTimer()
    timer.start(500)
    timer.timeout.connect(lambda: None)

    qapp.exec_()

if __name__ == '__main__':
    main()
