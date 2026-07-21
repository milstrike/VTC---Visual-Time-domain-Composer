import sys
import numpy as np
import pandas as pd
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QHBoxLayout, QVBoxLayout,
    QFormLayout, QGroupBox, QComboBox, QDoubleSpinBox, QSpinBox,
    QPushButton, QFileDialog, QSplitter, QMessageBox, QLabel
)
from PyQt5.QtCore import Qt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure


TRANSLATIONS = {
    "English": {
        "title": "VTC - Visual Time-domain Composer",
        "lang_select": "Language / 語言 / 言語:",
        "main_param": "Main Signal Parameters",
        "freq": "Frequency:",
        "amp": "Amplitude:",
        "phase": "Phase:",
        "offset": "DC Offset:",
        "duty": "Duty Cycle (Square/Tri):",
        "damping": "Damping Factor:",
        "time_param": "Sampling & Time Settings",
        "duration": "Duration:",
        "sample_rate": "Sample Rate:",
        "view_layout": "Waveform Display Layout (Side 2)",
        "display_mode": "Display Mode:",
        "single_signal": "Single Signal:",
        "export_group": "Export / Save Waveform",
        "save_img": "Save Image (PNG / JPG)",
        "save_csv": "Save Data (CSV)",
        "modes": [
            "1 Layout (Overlay All Signals)",
            "1 Layout (Select Single Signal)",
            "2 Subplot Layout",
            "4 Subplot Layout (2x2 Grid)",
            "Multi-Subplot (All Waveform Variations)"
        ],
        "wave_names": {
            "Sinusoidal": "Sinusoidal",
            "Square": "Square Wave",
            "Sawtooth": "Sawtooth Wave",
            "Triangle": "Triangle Wave",
            "Damped Sine": "Damped Sine",
            "Chirp (Frequency Sweep)": "Chirp (Frequency Sweep)",
            "Gaussian Pulse": "Gaussian Pulse",
            "White Noise": "White Noise"
        },
        "plot_titles": {
            "overlay": "Overlay of All Waveform Variations",
            "single": "Waveform: ",
            "time_label": "Time (s)",
            "amp_label": "Amplitude"
        },
        "dialogs": {
            "img_title": "Save Waveform as Image",
            "csv_title": "Save Waveform Data to CSV",
            "success_title": "Success",
            "success_img_msg": "Image successfully saved to:\n",
            "success_csv_msg": "CSV data successfully saved to:\n",
            "error_title": "Error",
            "error_save_msg": "Failed to save file: "
        }
    },
    "Bahasa Indonesia": {
        "title": "VTC - Visual Time-domain Composer",
        "lang_select": "Language / 語言 / 言語:",
        "main_param": "Parameter Sinyal Utama",
        "freq": "Frekuensi:",
        "amp": "Amplitudo:",
        "phase": "Fase (Phase):",
        "offset": "DC Offset:",
        "duty": "Duty Cycle (Kotak/Segitiga):",
        "damping": "Faktor Redaman (Damping):",
        "time_param": "Pengaturan Waktu & Sampling",
        "duration": "Durasi Waktu:",
        "sample_rate": "Sample Rate:",
        "view_layout": "Layout Penampil Waveform (Side 2)",
        "display_mode": "Mode Tampilan:",
        "single_signal": "Sinyal Tunggal:",
        "export_group": "Ekspor / Simpan Waveform",
        "save_img": "Simpan Gambar (PNG / JPG)",
        "save_csv": "Simpan Data (CSV)",
        "modes": [
            "1 Layout (Tumpuk Semua Sinyal / Overlay)",
            "1 Layout (Pilih Satu Sinyal)",
            "2 Subplot Layout",
            "4 Subplot Layout (2x2 Grid)",
            "Multi-Subplot (Semua Variasi Sinyal)"
        ],
        "wave_names": {
            "Sinusoidal": "Sinusoidal",
            "Square": "Sinyal Kotak (Square)",
            "Sawtooth": "Sinyal Gergaji (Sawtooth)",
            "Triangle": "Sinyal Segitiga (Triangle)",
            "Damped Sine": "Sinus Terredam (Damped Sine)",
            "Chirp (Frequency Sweep)": "Chirp (Sapu Frekuensi)",
            "Gaussian Pulse": "Puls Gaussian",
            "White Noise": "Noise Putih (White Noise)"
        },
        "plot_titles": {
            "overlay": "Overlay Semua Variasi Waveform",
            "single": "Waveform: ",
            "time_label": "Waktu (s)",
            "amp_label": "Amplitudo"
        },
        "dialogs": {
            "img_title": "Simpan Waveform sebagai Gambar",
            "csv_title": "Simpan Data Waveform ke CSV",
            "success_title": "Berhasil",
            "success_img_msg": "Gambar berhasil disimpan ke:\n",
            "success_csv_msg": "Data CSV berhasil disimpan ke:\n",
            "error_title": "Gagal",
            "error_save_msg": "Gagal menyimpan file: "
        }
    },
    "繁體中文": {
        "title": "VTC - Visual Time-domain Composer",
        "lang_select": "Language / 語言 / 言語:",
        "main_param": "主要信號參數",
        "freq": "頻率:",
        "amp": "振幅:",
        "phase": "相位:",
        "offset": "直流偏移 (DC Offset):",
        "duty": "工作週期 (Duty Cycle):",
        "damping": "阻尼係數 (Damping):",
        "time_param": "取樣與時間設定",
        "duration": "時間長度:",
        "sample_rate": "取樣率 (Sample Rate):",
        "view_layout": "波形顯示佈局 (Side 2)",
        "display_mode": "顯示模式:",
        "single_signal": "單一信號:",
        "export_group": "匯出 / 儲存波形",
        "save_img": "儲存影像 (PNG / JPG)",
        "save_csv": "儲存數據 (CSV)",
        "modes": [
            "1 個佈局 (疊加所有波形)",
            "1 個佈局 (選擇單一波形)",
            "2 子圖佈局",
            "4 子圖佈局 (2x2 網格)",
            "多子圖 (所有變體波形)"
        ],
        "wave_names": {
            "Sinusoidal": "正弦波 (Sinusoidal)",
            "Square": "方波 (Square Wave)",
            "Sawtooth": "鋸齒波 (Sawtooth Wave)",
            "Triangle": "三角波 (Triangle Wave)",
            "Damped Sine": "阻尼正弦波 (Damped Sine)",
            "Chirp (Frequency Sweep)": "掃頻信號 (Chirp)",
            "Gaussian Pulse": "高斯脈衝 (Gaussian Pulse)",
            "White Noise": "白雜訊 (White Noise)"
        },
        "plot_titles": {
            "overlay": "所有波形變體疊加顯示",
            "single": "波形: ",
            "time_label": "時間 (秒)",
            "amp_label": "振幅"
        },
        "dialogs": {
            "img_title": "將波形儲存為圖片",
            "csv_title": "將波形數據儲存為 CSV",
            "success_title": "成功",
            "success_img_msg": "圖片已成功儲存至:\n",
            "success_csv_msg": "CSV 數據已成功儲存至:\n",
            "error_title": "錯誤",
            "error_save_msg": "儲存檔案失敗: "
        }
    },
    "简体中文": {
        "title": "VTC - Visual Time-domain Composer",
        "lang_select": "Language / 语言 / 言语:",
        "main_param": "主要信号参数",
        "freq": "频率:",
        "amp": "振幅:",
        "phase": "相位:",
        "offset": "直流偏移 (DC Offset):",
        "duty": "占空比 (Duty Cycle):",
        "damping": "阻尼系数 (Damping):",
        "time_param": "采样与时间设置",
        "duration": "时间长度:",
        "sample_rate": "采样率 (Sample Rate):",
        "view_layout": "波形显示布局 (Side 2)",
        "display_mode": "显示模式:",
        "single_signal": "单一信号:",
        "export_group": "导出 / 保存波形",
        "save_img": "保存图像 (PNG / JPG)",
        "save_csv": "保存数据 (CSV)",
        "modes": [
            "1 个布局 (叠加所有波形)",
            "1 个布局 (选择单一波形)",
            "2 子图布局",
            "4 子图布局 (2x2 网格)",
            "多子图 (所有变体波形)"
        ],
        "wave_names": {
            "Sinusoidal": "正弦波 (Sinusoidal)",
            "Square": "方波 (Square Wave)",
            "Sawtooth": "锯齿波 (Sawtooth Wave)",
            "Triangle": "三角波 (Triangle Wave)",
            "Damped Sine": "阻尼正弦波 (Damped Sine)",
            "Chirp (Frequency Sweep)": "扫频信号 (Chirp)",
            "Gaussian Pulse": "高斯脉冲 (Gaussian Pulse)",
            "White Noise": "白噪声 (White Noise)"
        },
        "plot_titles": {
            "overlay": "所有波形变体叠加显示",
            "single": "波形: ",
            "time_label": "时间 (秒)",
            "amp_label": "振幅"
        },
        "dialogs": {
            "img_title": "将波形保存为图片",
            "csv_title": "将波形数据保存为 CSV",
            "success_title": "成功",
            "success_img_msg": "图片已成功保存至:\n",
            "success_csv_msg": "CSV 数据已成功保存至:\n",
            "error_title": "错误",
            "error_save_msg": "保存文件失败: "
        }
    },
    "日本語": {
        "title": "VTC - Visual Time-domain Composer",
        "lang_select": "Language / 言語:",
        "main_param": "メイン信号パラメータ",
        "freq": "周波数:",
        "amp": "振幅:",
        "phase": "位相:",
        "offset": "DCオフセット:",
        "duty": "デューティ比 (Duty Cycle):",
        "damping": "減衰係数 (Damping):",
        "time_param": "サンプリング & 時間設定",
        "duration": "時間長:",
        "sample_rate": "サンプリングレート:",
        "view_layout": "波形表示レイアウト (Side 2)",
        "display_mode": "表示モード:",
        "single_signal": "単一信号:",
        "export_group": "エクスポート / 保存",
        "save_img": "画像を保存 (PNG / JPG)",
        "save_csv": "データを保存 (CSV)",
        "modes": [
            "1レイアウト (全信号オーバーレイ)",
            "1レイアウト (単一信号選択)",
            "2サブプロットレイアウト",
            "4サブプロットレイアウト (2x2グリッド)",
            "マルチサブプロット (全波形バリエーション)"
        ],
        "wave_names": {
            "Sinusoidal": "正弦波 (Sinusoidal)",
            "Square": "矩形波 (Square Wave)",
            "Sawtooth": "鋸波 (Sawtooth Wave)",
            "Triangle": "三角波 (Triangle Wave)",
            "Damped Sine": "減衰振動波 (Damped Sine)",
            "Chirp (Frequency Sweep)": "チャープ信号 (Chirp)",
            "Gaussian Pulse": "ガウスパルス (Gaussian Pulse)",
            "White Noise": "ホワイトノイズ (White Noise)"
        },
        "plot_titles": {
            "overlay": "全波形バリエーションのオーバーレイ表示",
            "single": "波形: ",
            "time_label": "時間 (秒)",
            "amp_label": "振幅"
        },
        "dialogs": {
            "img_title": "波形を画像として保存",
            "csv_title": "波形データを CSV に保存",
            "success_title": "成功",
            "success_img_msg": "画像が正常に保存されました:\n",
            "success_csv_msg": "CSV データが正常に保存されました:\n",
            "error_title": "エラー",
            "error_save_msg": "ファイルの保存に失敗しました: "
        }
    }
}


class WaveformApp(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.current_lang = "English"

        self.resize(1200, 700)

        main_widget = QWidget()
        self.setCentralWidget(main_widget)
        main_layout = QHBoxLayout(main_widget)

        self.splitter = QSplitter(Qt.Horizontal)
        main_layout.addWidget(self.splitter)

        self.panel_side1 = QWidget()
        self.layout_side1 = QVBoxLayout(self.panel_side1)
        
        self.panel_side2 = QWidget()
        self.layout_side2 = QVBoxLayout(self.panel_side2)

        self.splitter.addWidget(self.panel_side1)
        self.splitter.addWidget(self.panel_side2)
        self.splitter.setSizes([360, 840])

        self.figure = Figure(figsize=(8, 6), dpi=100)
        self.canvas = FigureCanvas(self.figure)
        self.layout_side2.addWidget(self.canvas)

        self.wave_keys = [
            "Sinusoidal", "Square", "Sawtooth", "Triangle", 
            "Damped Sine", "Chirp (Frequency Sweep)", "Gaussian Pulse", "White Noise"
        ]
        
        self.active_signals = {}
        self.time_axis = None

        self.init_side1_ui()
        self.retranslate_ui()
        self.update_waveforms()

    def init_side1_ui(self):
        self.group_lang = QGroupBox()
        form_lang = QFormLayout()
        self.combo_lang = QComboBox()
        self.combo_lang.addItems([
            "English", 
            "Bahasa Indonesia", 
            "繁體中文", 
            "简体中文", 
            "日本語"
        ])
        self.combo_lang.setCurrentText("English")
        self.label_lang = QLabel()
        form_lang.addRow(self.label_lang, self.combo_lang)
        self.group_lang.setLayout(form_lang)
        self.layout_side1.addWidget(self.group_lang)

        self.group_param = QGroupBox()
        self.form_param = QFormLayout()

        self.spin_freq = QDoubleSpinBox()
        self.spin_freq.setRange(0.1, 10000.0)
        self.spin_freq.setValue(5.0)
        self.spin_freq.setSuffix(" Hz")
        self.spin_freq.setSingleStep(0.5)

        self.spin_amp = QDoubleSpinBox()
        self.spin_amp.setRange(0.0, 1000.0)
        self.spin_amp.setValue(1.0)
        self.spin_amp.setSingleStep(0.1)

        self.spin_phase = QDoubleSpinBox()
        self.spin_phase.setRange(-360.0, 360.0)
        self.spin_phase.setValue(0.0)
        self.spin_phase.setSuffix(" °")

        self.spin_offset = QDoubleSpinBox()
        self.spin_offset.setRange(-500.0, 500.0)
        self.spin_offset.setValue(0.0)

        self.spin_duty = QDoubleSpinBox()
        self.spin_duty.setRange(1.0, 99.0)
        self.spin_duty.setValue(50.0)
        self.spin_duty.setSuffix(" %")

        self.spin_damping = QDoubleSpinBox()
        self.spin_damping.setRange(0.0, 50.0)
        self.spin_damping.setValue(1.0)

        self.form_param.addRow("", self.spin_freq)
        self.form_param.addRow("", self.spin_amp)
        self.form_param.addRow("", self.spin_phase)
        self.form_param.addRow("", self.spin_offset)
        self.form_param.addRow("", self.spin_duty)
        self.form_param.addRow("", self.spin_damping)

        self.group_param.setLayout(self.form_param)
        self.layout_side1.addWidget(self.group_param)

        self.group_time = QGroupBox()
        self.form_time = QFormLayout()

        self.spin_duration = QDoubleSpinBox()
        self.spin_duration.setRange(0.01, 100.0)
        self.spin_duration.setValue(2.0)
        self.spin_duration.setSuffix(" s")

        self.spin_sr = QSpinBox()
        self.spin_sr.setRange(100, 100000)
        self.spin_sr.setValue(2000)
        self.spin_sr.setSuffix(" Hz")

        self.form_time.addRow("", self.spin_duration)
        self.form_time.addRow("", self.spin_sr)

        self.group_time.setLayout(self.form_time)
        self.layout_side1.addWidget(self.group_time)

        self.group_view = QGroupBox()
        self.form_view = QFormLayout()

        self.combo_layout = QComboBox()
        self.combo_single_select = QComboBox()

        self.form_view.addRow("", self.combo_layout)
        self.form_view.addRow("", self.combo_single_select)

        self.group_view.setLayout(self.form_view)
        self.layout_side1.addWidget(self.group_view)

        self.group_export = QGroupBox()
        layout_export = QVBoxLayout()

        self.btn_save_img = QPushButton()
        self.btn_save_csv = QPushButton()

        self.btn_save_img.clicked.connect(self.export_image)
        self.btn_save_csv.clicked.connect(self.export_csv)

        layout_export.addWidget(self.btn_save_img)
        layout_export.addWidget(self.btn_save_csv)
        self.group_export.setLayout(layout_export)

        self.layout_side1.addWidget(self.group_export)
        self.layout_side1.addStretch()

        input_widgets = [
            self.spin_freq, self.spin_amp, self.spin_phase, self.spin_offset,
            self.spin_duty, self.spin_damping, self.spin_duration, self.spin_sr
        ]
        for w in input_widgets:
            w.valueChanged.connect(self.update_waveforms)

        self.combo_layout.currentIndexChanged.connect(self.update_waveforms)
        self.combo_single_select.currentIndexChanged.connect(self.update_waveforms)
        self.combo_lang.currentIndexChanged.connect(self.on_language_change)

    def on_language_change(self):
        self.current_lang = self.combo_lang.currentText()
        self.retranslate_ui()
        self.update_waveforms()

    def retranslate_ui(self):
        t = TRANSLATIONS[self.current_lang]

        self.setWindowTitle(t["title"])
        self.label_lang.setText(t["lang_select"])

        self.group_param.setTitle(t["main_param"])
        self.group_time.setTitle(t["time_param"])
        self.group_view.setTitle(t["view_layout"])
        self.group_export.setTitle(t["export_group"])

        def set_form_label(form_layout, row_idx, text):
            label_item = form_layout.itemAt(row_idx, QFormLayout.LabelRole)
            if label_item and label_item.widget():
                label_item.widget().setText(text)
            else:
                form_layout.setWidget(row_idx, QFormLayout.LabelRole, QLabel(text))

        set_form_label(self.form_param, 0, t["freq"])
        set_form_label(self.form_param, 1, t["amp"])
        set_form_label(self.form_param, 2, t["phase"])
        set_form_label(self.form_param, 3, t["offset"])
        set_form_label(self.form_param, 4, t["duty"])
        set_form_label(self.form_param, 5, t["damping"])

        set_form_label(self.form_time, 0, t["duration"])
        set_form_label(self.form_time, 1, t["sample_rate"])

        set_form_label(self.form_view, 0, t["display_mode"])
        set_form_label(self.form_view, 1, t["single_signal"])

        curr_mode_idx = self.combo_layout.currentIndex()
        self.combo_layout.blockSignals(True)
        self.combo_layout.clear()
        self.combo_layout.addItems(t["modes"])
        self.combo_layout.setCurrentIndex(max(0, curr_mode_idx))
        self.combo_layout.blockSignals(False)

        curr_single_idx = self.combo_single_select.currentIndex()
        self.combo_single_select.blockSignals(True)
        self.combo_single_select.clear()
        translated_wave_names = [t["wave_names"][k] for k in self.wave_keys]
        self.combo_single_select.addItems(translated_wave_names)
        self.combo_single_select.setCurrentIndex(max(0, curr_single_idx))
        self.combo_single_select.blockSignals(False)

        self.btn_save_img.setText(t["save_img"])
        self.btn_save_csv.setText(t["save_csv"])

    def generate_signals(self):
        freq = self.spin_freq.value()
        amp = self.spin_amp.value()
        phase_rad = np.radians(self.spin_phase.value())
        offset = self.spin_offset.value()
        duty = self.spin_duty.value() / 100.0
        damping = self.spin_damping.value()
        duration = self.spin_duration.value()
        sr = self.spin_sr.value()

        total_samples = int(duration * sr)
        self.time_axis = np.linspace(0, duration, total_samples, endpoint=False)
        t = self.time_axis
        wt = 2 * np.pi * freq * t + phase_rad

        self.active_signals = {
            "Sinusoidal": amp * np.sin(wt) + offset,
            "Square": amp * np.where((wt / (2 * np.pi)) % 1.0 < duty, 1.0, -1.0) + offset,
            "Sawtooth": amp * (2 * ((wt / (2 * np.pi)) % 1.0) - 1) + offset,
            "Triangle": amp * (2 * np.abs(2 * ((wt / (2 * np.pi) + 0.25) % 1.0) - 1) - 1) + offset,
            "Damped Sine": amp * np.exp(-damping * t) * np.sin(wt) + offset,
            "Chirp (Frequency Sweep)": amp * np.sin(2 * np.pi * (freq + freq * 2 * t) * t + phase_rad) + offset,
            "Gaussian Pulse": amp * np.exp(-0.5 * ((t - duration / 2.0) / (0.1 / (freq + 1e-5)))**2) * np.cos(wt) + offset,
            "White Noise": amp * (2 * np.random.rand(len(t)) - 1) + offset
        }

    def update_waveforms(self):
        self.generate_signals()
        self.figure.clear()

        t = TRANSLATIONS[self.current_lang]
        mode = self.combo_layout.currentIndex()

        if mode == 0:  # Overlay
            ax = self.figure.add_subplot(111)
            for key, data in self.active_signals.items():
                label_name = t["wave_names"][key]
                ax.plot(self.time_axis, data, label=label_name)
            ax.set_title(t["plot_titles"]["overlay"])
            ax.set_xlabel(t["plot_titles"]["time_label"])
            ax.set_ylabel(t["plot_titles"]["amp_label"])
            ax.grid(True, linestyle="--", alpha=0.6)
            ax.legend(loc="upper right", fontsize='small')

        elif mode == 1:  # Single Signal
            ax = self.figure.add_subplot(111)
            selected_idx = self.combo_single_select.currentIndex()
            selected_key = self.wave_keys[selected_idx]
            selected_name = t["wave_names"][selected_key]
            
            ax.plot(self.time_axis, self.active_signals[selected_key], color='tab:blue')
            ax.set_title(f"{t['plot_titles']['single']}{selected_name}")
            ax.set_xlabel(t["plot_titles"]["time_label"])
            ax.set_ylabel(t["plot_titles"]["amp_label"])
            ax.grid(True, linestyle="--", alpha=0.6)

        elif mode == 2:  # Split 2 Layout
            ax1 = self.figure.add_subplot(211)
            ax2 = self.figure.add_subplot(212)
            
            ax1.plot(self.time_axis, self.active_signals["Sinusoidal"], color='tab:blue')
            ax1.set_title(t["wave_names"]["Sinusoidal"])
            ax1.grid(True, linestyle="--", alpha=0.6)

            ax2.plot(self.time_axis, self.active_signals["Square"], color='tab:orange')
            ax2.set_title(t["wave_names"]["Square"])
            ax2.grid(True, linestyle="--", alpha=0.6)
            ax2.set_xlabel(t["plot_titles"]["time_label"])

        elif mode == 3:  # 4 Subplot Grid
            keys = ["Sinusoidal", "Square", "Sawtooth", "Triangle"]
            colors = ['tab:blue', 'tab:orange', 'tab:green', 'tab:red']
            
            for i, key in enumerate(keys):
                ax = self.figure.add_subplot(2, 2, i + 1)
                ax.plot(self.time_axis, self.active_signals[key], color=colors[i])
                ax.set_title(t["wave_names"][key])
                ax.grid(True, linestyle="--", alpha=0.6)

        elif mode == 4:  # Multi-Subplot All
            num_signals = len(self.active_signals)
            for i, key in enumerate(self.wave_keys):
                ax = self.figure.add_subplot(num_signals, 1, i + 1)
                ax.plot(self.time_axis, self.active_signals[key])
                ax.set_ylabel(t["wave_names"][key], rotation=0, labelpad=50, fontsize=7)
                ax.grid(True, linestyle="--", alpha=0.5)
                if i < num_signals - 1:
                    ax.set_xticklabels([])
                else:
                    ax.set_xlabel(t["plot_titles"]["time_label"])

        self.figure.tight_layout()
        self.canvas.draw()

    def export_image(self):
        t = TRANSLATIONS[self.current_lang]["dialogs"]
        options = QFileDialog.Options()
        file_path, _ = QFileDialog.getSaveFileName(
            self, t["img_title"], "",
            "PNG Image (*.png);;JPEG Image (*.jpg *.jpeg)", options=options
        )
        if file_path:
            try:
                self.figure.savefig(file_path, dpi=300)
                QMessageBox.information(self, t["success_title"], f"{t['success_img_msg']}{file_path}")
            except Exception as e:
                QMessageBox.critical(self, t["error_title"], f"{t['error_save_msg']}{str(e)}")

    def export_csv(self):
        t = TRANSLATIONS[self.current_lang]["dialogs"]
        options = QFileDialog.Options()
        file_path, _ = QFileDialog.getSaveFileName(
            self, t["csv_title"], "",
            "CSV Files (*.csv)", options=options
        )
        if file_path:
            try:
                df_data = {"Time_s": self.time_axis}
                for key, data in self.active_signals.items():
                    df_data[key] = data
                
                df = pd.DataFrame(df_data)
                df.to_csv(file_path, index=False)
                QMessageBox.information(self, t["success_title"], f"{t['success_csv_msg']}{file_path}")
            except Exception as e:
                QMessageBox.critical(self, t["error_title"], f"{t['error_save_msg']}{str(e)}")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = WaveformApp()
    window.show()
    sys.exit(app.exec_())
