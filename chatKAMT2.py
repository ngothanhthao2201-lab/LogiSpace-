import streamlit as st

# Cấu hình trang Streamlit mở rộng toàn màn hình (wide mode)
st.set_page_config(
    page_title="LogiSpace — Freight Quotation & Space Intelligence Platform",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Khối mã HTML/CSS/JS với layout toàn màn hình (Full-width container)
html_code = """
<!DOCTYPE html>
<html lang="vi">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>LogiSpace — Freight Quotation & Space Intelligence Platform</title>
    <!-- Tailwind CSS CDN -->
    <script src="https://cdn.tailwindcss.com"></script>
    <!-- FontAwesome Icons CDN -->
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <!-- Vue.js 3 CDN -->
    <script src="https://unpkg.com/vue@3/dist/vue.global.js"></script>
    <style>
        /* Tùy chỉnh để chiếm toàn bộ màn hình trình duyệt */
        html, body {
            width: 100%;
            height: 100%;
            margin: 0;
            padding: 0;
            background-color: #0f172a;
        }
    </style>
</head>
<body class="bg-slate-900 text-slate-100 font-sans min-h-screen">

    <div id="app" class="flex flex-col min-h-screen w-full">
        <!-- Header / Navigation (Full Width) -->
        <header class="border-b border-slate-800 bg-slate-950/90 backdrop-blur sticky top-0 z-50 w-full px-6 py-3">
            <div class="w-full flex flex-col md:flex-row justify-between items-center gap-3">
                <div class="flex items-center gap-3">
                    <div class="bg-blue-600 text-white p-2.5 rounded-xl font-bold shadow-lg shadow-blue-600/30">
                        <i class="fa-solid fa-ship"></i>
                    </div>
                    <div>
                        <h1 class="font-bold text-base md:text-lg leading-none text-blue-400">LogiSpace Platform</h1>
                        <span class="text-xs text-slate-400">Freight Quotation & Space Intelligence Platform</span>
                    </div>
                </div>
                
                <!-- Navigation Tabs -->
                <div class="flex flex-wrap items-center gap-1 bg-slate-900 p-1 rounded-xl border border-slate-800">
                    <button @click="currentTab = 'dashboard'" :class="currentTab === 'dashboard' ? 'bg-blue-600 text-white shadow' : 'text-slate-400 hover:text-slate-200'" class="px-3.5 py-1.5 rounded-lg text-xs font-medium transition">
                        <i class="fa-solid fa-chart-pie mr-1"></i> Dashboard
                    </button>
                    <button @click="currentTab = 'quotation'" :class="currentTab === 'quotation' ? 'bg-blue-600 text-white shadow' : 'text-slate-400 hover:text-slate-200'" class="px-3.5 py-1.5 rounded-lg text-xs font-medium transition">
                        <i class="fa-solid fa-calculator mr-1"></i> Báo Giá & Lợi Nhuận
                    </button>
                    <button @click="currentTab = 'spaceForecast'" :class="currentTab === 'spaceForecast' ? 'bg-blue-600 text-white shadow' : 'text-slate-400 hover:text-slate-200'" class="px-3.5 py-1.5 rounded-lg text-xs font-medium transition">
                        <i class="fa-solid fa-shield-halved mr-1"></i> Dự Báo Space
                    </button>
                    <button @click="currentTab = 'peakSeason'" :class="currentTab === 'peakSeason' ? 'bg-blue-600 text-white shadow' : 'text-slate-400 hover:text-slate-200'" class="px-3.5 py-1.5 rounded-lg text-xs font-medium transition">
                        <i class="fa-solid fa-triangle-exclamation mr-1"></i> Mùa Cao Điểm
                    </button>
                    <button @click="currentTab = 'marketplace'" :class="currentTab === 'marketplace' ? 'bg-blue-600 text-white shadow' : 'text-slate-400 hover:text-slate-200'" class="px-3.5 py-1.5 rounded-lg text-xs font-medium transition">
                        <i class="fa-solid fa-right-left mr-1"></i> Sàn Slot Marketplace
                    </button>
                </div>
            </div>
        </header>

        <!-- Main Workspace (Full Width Container) -->
        <main class="flex-1 w-full p-4 md:p-6 space-y-6">

            <!-- BANNER TRẠNG THÁI DỮ LIỆU & DEMO MODE -->
            <div class="bg-slate-800/80 border border-slate-700 rounded-2xl p-4 flex flex-col md:flex-row items-center justify-between gap-3 text-xs shadow-lg w-full">
                <div class="flex items-center gap-3">
                    <span class="w-2.5 h-2.5 rounded-full bg-amber-400 animate-pulse"></span>
                    <div>
                        <strong class="text-white">Trạng thái hệ thống:</strong> Đang hoạt động ở <strong>Chế độ DEMO / Dữ liệu thủ công</strong> (Hiển thị toàn màn hình).
                    </div>
                </div>
                <div class="flex items-center gap-3 text-slate-400">
                    <span>Cập nhật gần nhất: <strong class="text-slate-200">Hôm nay</strong></span>
                    <button @click="loadSampleData" class="bg-blue-600/20 hover:bg-blue-600/30 text-blue-400 border border-blue-500/30 px-3 py-1 rounded-lg transition font-medium">
                        Nạp Dữ Liệu Mẫu
                    </button>
                </div>
            </div>

            <!-- TAB 1: DASHBOARD TỔNG QUAN THỊ TRƯỜNG -->
            <div v-if="currentTab === 'dashboard'" class="space-y-6 w-full">
                <div class="grid grid-cols-1 md:grid-cols-4 gap-4 w-full">
                    <div class="bg-slate-800/60 border border-slate-700/60 rounded-2xl p-5 shadow-lg">
                        <div class="text-xs text-slate-400 mb-1">Tổng Số RFQ Đang Xử Lý</div>
                        <div class="text-2xl font-bold text-white">12 Hồ Sơ</div>
                        <div class="text-[11px] text-emerald-400 mt-2"><i class="fa-solid fa-arrow-up mr-1"></i> +3 hồ sơ trong tuần</div>
                    </div>
                    <div class="bg-slate-800/60 border border-slate-700/60 rounded-2xl p-5 shadow-lg">
                        <div class="text-xs text-slate-400 mb-1">Mục Tiêu Biên Lợi Nhuận</div>
                        <div class="text-2xl font-bold text-blue-400">{{ targetMargin }}%</div>
                        <div class="text-[11px] text-slate-400 mt-2">Ngưỡng tối thiểu chuẩn Sales</div>
                    </div>
                    <div class="bg-slate-800/60 border border-slate-700/60 rounded-2xl p-5 shadow-lg">
                        <div class="text-xs text-slate-400 mb-1">Nguy Cơ Thiếu Space Tuyến US</div>
                        <div class="text-2xl font-bold text-amber-400">Rất Cao (85%)</div>
                        <div class="text-[11px] text-amber-300 mt-2">Đỉnh điểm front-loading</div>
                    </div>
                    <div class="bg-slate-800/60 border border-slate-700/60 rounded-2xl p-5 shadow-lg">
                        <div class="text-xs text-slate-400 mb-1">Slot Sẵn Sàng Trên Sàn</div>
                        <div class="text-2xl font-bold text-emerald-400">14 Containers</div>
                        <div class="text-[11px] text-slate-400 mt-2">Từ các đối tác Forwarder</div>
                    </div>
                </div>

                <div class="grid grid-cols-1 lg:grid-cols-2 gap-6 w-full">
                    <div class="bg-slate-800/80 border border-slate-700/80 rounded-2xl p-5 shadow-xl space-y-4">
                        <h3 class="text-sm font-bold text-slate-200 flex items-center gap-2">
                            <i class="fa-solid fa-bolt text-amber-400"></i> Cảnh Báo Nhanh Cho Sales Forwarding
                        </h3>
                        <div class="space-y-3 text-xs">
                            <div class="p-3 bg-rose-500/10 border border-rose-500/30 rounded-xl text-rose-300 flex items-start gap-2.5">
                                <i class="fa-solid fa-triangle-exclamation mt-0.5"></i>
                                <div>
                                    <strong class="block text-white">Tuyến Cái Mép → Los Angeles căng thẳng space</strong>
                                    <span>Nhu cầu booking tăng đột biến 40%. Khuyến nghị chốt allotment trước 14 ngày để tránh rủi ro roll-over.</span>
                                </div>
                            </div>
                        </div>
                    </div>

                    <div class="bg-slate-800/80 border border-slate-700/80 rounded-2xl p-5 shadow-xl space-y-4">
                        <h3 class="text-sm font-bold text-slate-200 flex items-center gap-2">
                            <i class="fa-solid fa-list-check text-blue-400"></i> Trạng Thái Hồ Sơ Gần Nhất
                        </h3>
                        <div class="overflow-x-auto text-xs w-full">
                            <table class="w-full text-left text-slate-300">
                                <thead class="bg-slate-900 text-slate-400 uppercase text-[10px]">
                                    <tr>
                                        <th class="p-2.5">Mã RFQ</th>
                                        <th class="p-2.5">Khách Hàng</th>
                                        <th class="p-2.5">Tuyến</th>
                                        <th class="p-2.5">Quy Mô</th>
                                        <th class="p-2.5 text-right">Biên Lãi</th>
                                    </tr>
                                </thead>
                                <tbody class="divide-y divide-slate-700/50">
                                    <tr>
                                        <td class="p-2.5 font-mono text-blue-400">RFQ-2026-001</td>
                                        <td class="p-2.5">QA Furniture</td>
                                        <td class="p-2.5">VNVUT → USLAX</td>
                                        <td class="p-2.5">5 x 40'HC</td>
                                        <td class="p-2.5 text-right font-bold text-emerald-400">12.5%</td>
                                    </tr>
                                </tbody>
                            </table>
                        </div>
                    </div>
                </div>
            </div>

            <!-- TAB 2: TRA CỨU BÁO GIÁ & PHÂN TÍCH LỢI NHUẬN -->
            <div v-if="currentTab === 'quotation'" class="space-y-6 w-full">
                <!-- Form nhập thông tin lô hàng -->
                <div class="bg-slate-800/80 border border-slate-700/80 rounded-2xl p-5 shadow-xl space-y-4 w-full">
                    <div class="flex justify-between items-center pb-3 border-b border-slate-700/60">
                        <h3 class="text-sm font-bold text-blue-400 flex items-center gap-2">
                            <i class="fa-solid fa-file-invoice-dollar"></i> Phân Hệ A: Lập Hồ Sơ Báo Giá Vận Tải Quốc Tế
                        </h3>
                        <span class="text-xs text-slate-400">Chuẩn hóa biên lợi nhuận tối thiểu: <strong>{{ targetMargin }}%</strong></span>
                    </div>

                    <div class="grid grid-cols-1 md:grid-cols-3 lg:grid-cols-6 gap-4 text-xs">
                        <div>
                            <label class="text-slate-400 block mb-1">Khách Hàng / Shipper</label>
                            <input type="text" v-model="shipment.shipper" class="w-full bg-slate-900 border border-slate-700 rounded-lg p-2 text-slate-100">
                        </div>
                        <div>
                            <label class="text-slate-400 block mb-1">Cảng Đi (POL)</label>
                            <input type="text" v-model="shipment.pol" class="w-full bg-slate-900 border border-slate-700 rounded-lg p-2 text-slate-100">
                        </div>
                        <div>
                            <label class="text-slate-400 block mb-1">Cảng Đến (POD)</label>
                            <input type="text" v-model="shipment.pod" class="w-full bg-slate-900 border border-slate-700 rounded-lg p-2 text-slate-100">
                        </div>
                        <div>
                            <label class="text-slate-400 block mb-1">Loại Container</label>
                            <select v-model="shipment.containerType" class="w-full bg-slate-900 border border-slate-700 rounded-lg p-2 text-slate-100">
                                <option value="40'HC">40'HC</option>
                                <option value="40'GP">40'GP</option>
                                <option value="20'GP">20'GP</option>
                                <option value="45'HC">45'HC</option>
                            </select>
                        </div>
                        <div>
                            <label class="text-slate-400 block mb-1">Số Lượng Cont</label>
                            <input type="number" min="1" v-model.number="shipment.volume" class="w-full bg-slate-900 border border-slate-700 rounded-lg p-2 text-amber-400 font-bold">
                        </div>
                        <div>
                            <label class="text-slate-400 block mb-1">Mục tiêu Biên Lợi Nhuận (%)</label>
                            <input type="number" min="1" max="50" v-model.number="targetMargin" class="w-full bg-slate-900 border border-slate-700 rounded-lg p-2 text-blue-400 font-bold">
                        </div>
                    </div>
                </div>

                <!-- So sánh phương án, tính giá bán tối thiểu & lợi nhuận -->
                <div class="bg-slate-800/80 border border-slate-700/80 rounded-2xl p-5 shadow-xl space-y-4 w-full">
                    <h3 class="text-sm font-bold text-emerald-400 flex items-center gap-2">
                        <i class="fa-solid fa-scale-balanced"></i> Phân Hệ B: Phân Tích Giá Vốn, Giá Bán Tối Thiểu & Biên Lợi Nhuận
                    </h3>

                    <div class="space-y-4 w-full">
                        <div v-for="carrier in evaluatedCarriers" :key="carrier.id" class="bg-slate-900/70 border border-slate-700/80 rounded-xl p-4 space-y-3 w-full">
                            <div class="flex flex-col md:flex-row md:items-center justify-between gap-3">
                                <div class="flex items-center gap-3">
                                    <div class="w-10 h-10 rounded-lg bg-slate-800 flex items-center justify-center font-bold text-slate-200 border border-slate-700">
                                        {{ carrier.code }}
                                    </div>
                                    <div>
                                        <div class="font-semibold text-slate-100 flex items-center gap-2">
                                            {{ carrier.name }}
                                            <span class="text-[10px] bg-blue-500/20 text-blue-300 px-2 py-0.5 rounded border border-blue-500/30">{{ carrier.vessel }}</span>
                                        </div>
                                        <div class="text-xs text-slate-400 mt-0.5">
                                            ETD: <strong class="text-slate-200">{{ carrier.etd }}</strong> | Trễ tàu: <span class="text-rose-400 font-semibold">+{{ carrier.delayDays }} ngày</span> | Space khả dụng: <strong :class="carrier.spaceAvailable >= shipment.volume ? 'text-emerald-400' : 'text-amber-400'">{{ carrier.spaceAvailable }}/{{ shipment.volume }} cont</strong>
                                        </div>
                                    </div>
                                </div>

                                <div class="text-right text-xs">
                                    <span class="text-slate-400 block">Giá Vốn Dự Kiến (1 Cont)</span>
                                    <span class="text-base font-bold text-blue-400">${{ carrier.totalCostPerCont.toLocaleString() }} USD</span>
                                </div>
                            </div>

                            <!-- Thành phần chi phí -->
                            <div class="grid grid-cols-2 md:grid-cols-5 gap-2 bg-slate-950/60 p-3 rounded-lg border border-slate-800 text-xs w-full">
                                <div>Cước biển (O/F): <strong class="text-slate-200">${{ carrier.oceanFreight }}</strong></div>
                                <div>Phụ phí PSS: <strong class="text-slate-200">${{ carrier.pss }}</strong></div>
                                <div>Local Charges: <strong class="text-slate-200">${{ carrier.localCharges }}</strong></div>
                                <div>Phí slot bổ sung: <strong class="text-slate-200">${{ carrier.extraSlotFee }}</strong></div>
                                <div>Dự phòng rủi ro: <strong class="text-slate-200">${{ carrier.reserveFee }}</strong></div>
                            </div>

                            <!-- Tài chính & Giá bán tối thiểu -->
                            <div class="pt-2 border-t border-slate-800 flex flex-col md:flex-row md:items-center justify-between gap-3 text-xs">
                                <div class="grid grid-cols-2 md:grid-cols-4 gap-6">
                                    <div>
                                        <span class="text-slate-400 block">Giá Bán Đề Xuất Hiện Tại</span>
                                        <span class="font-bold text-slate-100">${{ carrier.currentSellRate }} USD</span>
                                    </div>
                                    <div>
                                        <span class="text-slate-400 block">Giá Bán Tối Thiểu (Chuẩn {{ targetMargin }}%)</span>
                                        <span class="font-bold text-emerald-400">${{ carrier.minSellRateRequired }} USD</span>
                                    </div>
                                    <div>
                                        <span class="text-slate-400 block">Biên Lợi Nhuận Gộp</span>
                                        <span class="font-bold" :class="carrier.marginPercent >= targetMargin ? 'text-emerald-400' : 'text-amber-400'">
                                            {{ carrier.marginPercent }}%
                                        </span>
                                    </div>
                                    <div>
                                        <span class="text-slate-400 block">Tổng Lãi Toàn Lô</span>
                                        <span class="font-bold" :class="carrier.totalProfit >= 0 ? 'text-emerald-400' : 'text-rose-400'">${{ carrier.totalProfit.toLocaleString() }} USD</span>
                                    </div>
                                </div>

                                <div>
                                    <span v-if="carrier.marginPercent < targetMargin" class="px-2.5 py-1 rounded-lg bg-rose-500/20 text-rose-300 border border-rose-500/30 text-[11px] font-medium flex items-center gap-1">
                                        <i class="fa-solid fa-triangle-exclamation"></i> Dưới biên lãi mục tiêu
                                    </span>
                                    <span v-else class="px-2.5 py-1 rounded-lg bg-emerald-500/20 text-emerald-300 border border-emerald-500/30 text-[11px] font-medium flex items-center gap-1">
                                        <i class="fa-solid fa-circle-check"></i> Đạt chuẩn biên lãi
                                    </span>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>

            <!-- TAB 3: DỰ BÁO SPACE -->
            <div v-if="currentTab === 'spaceForecast'" class="space-y-6 w-full">
                <div class="bg-slate-800/80 border border-slate-700/80 rounded-2xl p-5 shadow-xl space-y-4 w-full">
                    <h3 class="text-sm font-bold text-amber-400 flex items-center gap-2">
                        <i class="fa-solid fa-shield-halved"></i> Phân Hệ C & D: Dự Báo Thiếu Hụt Space & Intelligence Mùa Cao Điểm
                    </h3>
                    <div class="p-4 bg-gradient-to-br from-amber-500/10 to-orange-500/10 rounded-xl border border-amber-500/30 text-xs text-slate-300">
                        <strong class="text-amber-400 text-sm block mb-1">Cảnh báo thị trường:</strong>
                        Thị trường xuất khẩu đang chứng kiến làn sóng đẩy hàng trước thời hạn thuế quan. Khuyến nghị chốt booking sớm trước 14 ngày để tránh rủi ro roll-over.
                    </div>
                </div>
            </div>

            <!-- TAB 4: MÙA CAO ĐIỂM -->
            <div v-if="currentTab === 'peakSeason'" class="space-y-6 w-full">
                <div class="bg-slate-800/80 border border-slate-700/80 rounded-2xl p-5 shadow-xl space-y-4 w-full">
                    <h3 class="text-sm font-bold text-amber-400 flex items-center gap-2">
                        <i class="fa-solid fa-chart-line"></i> Phân Hệ D: Biểu Đồ & Intelligence Mùa Cao Điểm Theo Tuyến
                    </h3>
                    <div class="space-y-3 text-xs text-slate-300">
                        <div class="p-4 bg-slate-900/60 rounded-xl border border-slate-700">
                            <div class="font-bold text-white text-sm mb-1">Mùa Đẩy Hàng Trước Thuế Quan (Tariff Front-loading)</div>
                            <p>Tuyến chịu ảnh hưởng: Việt Nam → Bờ Tây/Bờ Đông Hoa Kỳ. Thời gian: Tháng 4 đến tháng 6. Nguy cơ thiếu space nặng.</p>
                        </div>
                    </div>
                </div>
            </div>

            <!-- TAB 5: SÀN GIAO DỊCH SLOT SPACE -->
            <div v-if="currentTab === 'marketplace'" class="space-y-6 w-full">
                <div class="bg-slate-800/80 border border-slate-700/80 rounded-2xl p-5 shadow-xl space-y-4 w-full">
                    <div class="flex justify-between items-center pb-3 border-b border-slate-700/60">
                        <h3 class="text-sm font-bold text-emerald-400 flex items-center gap-2">
                            <i class="fa-solid fa-right-left"></i> Phân Hệ E: Sàn Giao Dịch Slot Space (Space Marketplace)
                        </h3>
                        <span class="text-xs text-slate-400">Kết nối nguồn cung slot dư thừa giữa các Forwarder</span>
                    </div>

                    <div class="grid grid-cols-1 md:grid-cols-2 gap-4 w-full">
                        <div v-for="slot in marketplaceList" :key="slot.id" class="bg-slate-900/70 border border-slate-700/80 rounded-xl p-4 flex flex-col justify-between gap-3 text-xs">
                            <div class="flex justify-between items-start">
                                <div>
                                    <span class="px-2 py-0.5 rounded bg-amber-500/10 text-amber-400 border border-amber-500/20 font-semibold">{{ slot.provider }}</span>
                                    <div class="font-semibold text-slate-100 mt-1.5">Hãng tàu: {{ slot.carrier }} (ETD: {{ slot.etd }})</div>
                                    <div class="text-slate-400">Tuyến: {{ slot.route }}</div>
                                </div>
                                <div class="text-right">
                                    <div class="text-slate-400">Giá nhượng</div>
                                    <div class="text-sm font-bold text-emerald-400">${{ slot.price }} USD/Cont</div>
                                </div>
                            </div>

                            <div class="flex justify-between items-center pt-2 border-t border-slate-800">
                                <span class="text-slate-300">Khả dụng: <strong>{{ slot.slots }} slot {{ shipment.containerType }}</strong></span>
                                <button @click="claimSlot(slot)" class="bg-emerald-600 hover:bg-emerald-500 text-white px-3 py-1.5 rounded-lg transition font-medium">
                                    Yêu Cầu Nhượng Slot (Demo)
                                </button>
                            </div>
                        </div>
                    </div>
                </div>
            </div>

        </main>
    </div>

    <!-- Script Vue.js 3 Logic -->
    <script>
        const { createApp } = Vue;

        createApp({
            data() {
                return {
                    currentTab: 'quotation',
                    targetMargin: 10,

                    shipment: {
                        shipper: 'QA Furniture Co., Ltd',
                        pol: 'Cái Mép (VNVUT)',
                        pod: 'Los Angeles (USLAX)',
                        containerType: "40'HC",
                        volume: 5
                    },

                    carriers: [
                        {
                            id: 1,
                            name: 'Wan Hai Lines',
                            code: 'WHL',
                            vessel: 'WAN HAI A01 E012',
                            etd: '10/06/2026',
                            delayDays: 2,
                            spaceAvailable: 3,
                            oceanFreight: 4800,
                            pss: 300,
                            localCharges: 100,
                            extraSlotFee: 0,
                            reserveFee: 30,
                            currentSellRate: 5438
                        },
                        {
                            id: 2,
                            name: 'Evergreen Line',
                            code: 'EMC',
                            vessel: 'EVER GIVEN / 0421E',
                            etd: '09/06/2026',
                            delayDays: 0,
                            spaceAvailable: 5,
                            oceanFreight: 4850,
                            pss: 300,
                            localCharges: 100,
                            extraSlotFee: 0,
                            reserveFee: 30,
                            currentSellRate: 5500
                        }
                    ],

                    marketplaceList: [
                        { id: 101, provider: 'VinaFreighter Logistics', carrier: 'Evergreen', route: 'Cái Mép → Los Angeles', etd: '08/06/2026', slots: 2, price: 5240 },
                        { id: 102, provider: 'Global Forwarding Partner', carrier: 'COSCO', route: 'Cái Mép → Long Beach', etd: '10/06/2026', slots: 3, price: 5220 }
                    ]
                }
            },
            computed: {
                evaluatedCarriers() {
                    return this.carriers.map(c => {
                        const totalCostPerCont = c.oceanFreight + c.pss + c.localCharges + c.extraSlotFee + c.reserveFee;
                        const minSellRateRequired = Math.ceil(totalCostPerCont / (1 - (this.targetMargin / 100)));
                        const profitPerCont = c.currentSellRate - totalCostPerCont;
                        const totalProfit = profitPerCont * this.shipment.volume;
                        const marginPercent = c.currentSellRate > 0 ? ((profitPerCont / c.currentSellRate) * 100).toFixed(2) : 0;

                        return {
                            ...c,
                            totalCostPerCont,
                            minSellRateRequired,
                            profitPerCont,
                            totalProfit,
                            marginPercent: parseFloat(marginPercent)
                        };
                    });
                }
            },
            methods: {
                loadSampleData() {
                    alert('Đã tải lại bộ dữ liệu mẫu kiểm thử tiêu chuẩn!');
                },
                claimSlot(slot) {
                    alert(`Đã gửi yêu cầu giữ ${slot.slots} slot từ ${slot.provider} (Thao tác DEMO thành công)!`);
                }
            }
        }).mount('#app');
    </script>
</body>
</html>
"""

# Render hiển thị chiếm toàn màn hình trong Streamlit
st.components.v1.html(html_code, height=950, scrolling=True)
