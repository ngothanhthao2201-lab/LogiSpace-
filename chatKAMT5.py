import streamlit as st

# Cấu hình trang Streamlit hiển thị toàn màn hình (wide layout)
st.set_page_config(
    page_title="LogiSpace Simulator — Freight Quotation & Space Intelligence Platform",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Khối mã HTML/CSS/JS toàn diện tích hợp State Management tập trung và đồng bộ hóa realtime
html_code = """
<!DOCTYPE html>
<html lang="vi">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>LogiSpace Simulator — Freight Quotation & Space Intelligence Platform</title>
    <!-- Tailwind CSS CDN -->
    <script src="https://cdn.tailwindcss.com"></script>
    <!-- FontAwesome Icons CDN -->
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <!-- Vue.js 3 CDN -->
    <script src="https://unpkg.com/vue@3/dist/vue.global.js"></script>
    <style>
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
        <!-- Header & Navigation -->
        <header class="border-b border-slate-800 bg-slate-950/90 backdrop-blur sticky top-0 z-50 w-full px-6 py-3">
            <div class="w-full flex flex-col md:flex-row justify-between items-center gap-3">
                <div class="flex items-center gap-3">
                    <div class="bg-blue-600 text-white p-2.5 rounded-xl font-bold shadow-lg shadow-blue-600/30">
                        <i class="fa-solid fa-ship"></i>
                    </div>
                    <div>
                        <h1 class="font-bold text-base md:text-lg leading-none text-blue-400">LogiSpace Simulator</h1>
                        <span class="text-xs text-slate-400">Freight Quotation & Space Intelligence Platform</span>
                    </div>
                </div>
                
                <!-- Navigation Tabs -->
                <div class="flex flex-wrap items-center gap-1 bg-slate-900 p-1 rounded-xl border border-slate-800">
                    <button @click="currentTab = 'dashboard'" :class="currentTab === 'dashboard' ? 'bg-blue-600 text-white shadow' : 'text-slate-400 hover:text-slate-200'" class="px-3.5 py-1.5 rounded-lg text-xs font-medium transition">
                        <i class="fa-solid fa-chart-pie mr-1"></i> Dashboard
                    </button>
                    <button @click="currentTab = 'shipmentForm'" :class="currentTab === 'shipmentForm' ? 'bg-blue-600 text-white shadow' : 'text-slate-400 hover:text-slate-200'" class="px-3.5 py-1.5 rounded-lg text-xs font-medium transition">
                        <i class="fa-solid fa-pen-to-square mr-1"></i> Thông Tin Lô Hàng
                    </button>
                    <button @click="currentTab = 'quotation'" :class="currentTab === 'quotation' ? 'bg-blue-600 text-white shadow' : 'text-slate-400 hover:text-slate-200'" class="px-3.5 py-1.5 rounded-lg text-xs font-medium transition">
                        <i class="fa-solid fa-calculator mr-1"></i> Báo Giá & Biên Lãi
                    </button>
                    <button @click="currentTab = 'spaceForecast'" :class="currentTab === 'spaceForecast' ? 'bg-blue-600 text-white shadow' : 'text-slate-400 hover:text-slate-200'" class="px-3.5 py-1.5 rounded-lg text-xs font-medium transition">
                        <i class="fa-solid fa-shield-halved mr-1"></i> Dự Báo Space
                    </button>
                    <button @click="currentTab = 'peakSeason'" :class="currentTab === 'peakSeason' ? 'bg-blue-600 text-white shadow' : 'text-slate-400 hover:text-slate-200'" class="px-3.5 py-1.5 rounded-lg text-xs font-medium transition">
                        <i class="fa-solid fa-triangle-exclamation mr-1"></i> Mùa Cao Điểm & Booking
                    </button>
                    <button @click="currentTab = 'marketplace'" :class="currentTab === 'marketplace' ? 'bg-blue-600 text-white shadow' : 'text-slate-400 hover:text-slate-200'" class="px-3.5 py-1.5 rounded-lg text-xs font-medium transition">
                        <i class="fa-solid fa-right-left mr-1"></i> Sàn Slot Marketplace
                    </button>
                </div>
            </div>
        </header>

        <!-- Main Workspace -->
        <main class="flex-1 w-full p-4 md:p-6 space-y-6">

            <!-- BANNER TRẠNG THÁI DỮ LIỆU & ĐỒNG BỘ -->
            <div class="bg-slate-800/80 border border-slate-700 rounded-2xl p-4 flex flex-col md:flex-row items-center justify-between gap-3 text-xs shadow-lg w-full">
                <div class="flex items-center gap-3">
                    <span class="w-2.5 h-2.5 rounded-full bg-emerald-400 animate-pulse"></span>
                    <div>
                        <strong class="text-white">Trạng thái đồng bộ:</strong> 
                        <span class="px-2 py-0.5 rounded bg-emerald-500/20 text-emerald-300 border border-emerald-500/30 font-medium">Toàn bộ phân hệ đã đồng bộ theo lô hàng xác nhận</span>
                        (Cập nhật lúc: <span class="text-slate-300 font-mono">{{ lastUpdatedTime }}</span> | Dữ liệu: MANUAL & DEMO DATA).
                    </div>
                </div>
                <div class="flex items-center gap-3">
                    <button @click="resetToDefault" class="bg-slate-700 hover:bg-slate-600 text-slate-200 px-3 py-1 rounded-lg transition font-medium">
                        Đặt Lại Dữ Liệu Mẫu
                    </button>
                </div>
            </div>

            <!-- TAB 1: DASHBOARD TỔNG QUAN -->
            <div v-if="currentTab === 'dashboard'" class="space-y-6 w-full">
                <div class="grid grid-cols-1 md:grid-cols-4 gap-4 w-full">
                    <div class="bg-slate-800/60 border border-slate-700/60 rounded-2xl p-5 shadow-lg">
                        <div class="text-xs text-slate-400 mb-1">Lô Hàng Đang Theo Dõi</div>
                        <div class="text-2xl font-bold text-white">{{ shipment.volume }} x {{ shipment.containerType }}</div>
                        <div class="text-[11px] text-blue-400 mt-2">Tuyến: {{ shipment.pol }} → {{ shipment.pod }}</div>
                    </div>
                    <div class="bg-slate-800/60 border border-slate-700/60 rounded-2xl p-5 shadow-lg">
                        <div class="text-xs text-slate-400 mb-1">Mục Tiêu Biên Lợi Nhuận</div>
                        <div class="text-2xl font-bold text-blue-400">{{ targetMargin }}%</div>
                        <div class="text-[11px] text-slate-400 mt-2">Ngưỡng chuẩn Sales Forwarding</div>
                    </div>
                    <div class="bg-slate-800/60 border border-slate-700/60 rounded-2xl p-5 shadow-lg">
                        <div class="text-xs text-slate-400 mb-1">Thiếu Hụt Space Tuyến Chọn</div>
                        <div class="text-2xl font-bold" :class="spaceDeficit > 0 ? 'text-rose-400' : 'text-emerald-400'">
                            {{ spaceDeficit }} Containers
                        </div>
                        <div class="text-[11px] text-slate-400 mt-2">Nhu cầu: {{ shipment.volume }} | Khả dụng: {{ availableAllocatedSpace }}</div>
                    </div>
                    <div class="bg-slate-800/60 border border-slate-700/60 rounded-2xl p-5 shadow-lg">
                        <div class="text-xs text-slate-400 mb-1">Slot Phù Hợp Trên Sàn</div>
                        <div class="text-2xl font-bold text-emerald-400">{{ filteredMarketplaceList.length }} Tin Đăng</div>
                        <div class="text-[11px] text-slate-400 mt-2">Đã lọc theo tuyến hiện hành</div>
                    </div>
                </div>

                <div class="grid grid-cols-1 lg:grid-cols-2 gap-6 w-full">
                    <div class="bg-slate-800/80 border border-slate-700/80 rounded-2xl p-5 shadow-xl space-y-4">
                        <h3 class="text-sm font-bold text-slate-200 flex items-center gap-2">
                            <i class="fa-solid fa-bolt text-amber-400"></i> Tổng Quan Hồ Sơ Xác Nhận Hiện Tại
                        </h3>
                        <div class="space-y-2 text-xs text-slate-300">
                            <div><strong>Shipper / Khách hàng:</strong> {{ shipment.shipper }} / {{ shipment.customer }}</div>
                            <div><strong>Hành trình (POL → POD):</strong> {{ shipment.pol }} → {{ shipment.pod }}</div>
                            <div><strong>Loại hàng hóa:</strong> {{ shipment.commodity }}</div>
                            <div><strong>Ngày hàng sẵn (CRD):</strong> {{ shipment.crd }} | <strong>ETD Dự Kiến:</strong> {{ shipment.etd }}</div>
                            <div class="p-3 mt-2 rounded-xl border" :class="spaceDeficit > 0 ? 'bg-rose-500/10 border-rose-500/30 text-rose-300' : 'bg-emerald-500/10 border-emerald-500/30 text-emerald-300'">
                                <i class="fa-solid fa-triangle-exclamation mr-1"></i> 
                                <span v-if="spaceDeficit > 0">Cảnh báo thiếu hụt {{ spaceDeficit }} container trên tuyến này! Cần xem xét tách lô hoặc mua bù từ Sàn Slot.</span>
                                <span v-else>Nguồn cung space đã xác minh đáp ứng đủ nhu cầu lô hàng.</span>
                            </div>
                        </div>
                    </div>

                    <div class="bg-slate-800/80 border border-slate-700/80 rounded-2xl p-5 shadow-xl space-y-4">
                        <h3 class="text-sm font-bold text-slate-200 flex items-center gap-2">
                            <i class="fa-solid fa-circle-info text-blue-400"></i> Quy Tắc Đồng Bộ Dữ Liệu
                        </h3>
                        <p class="text-xs text-slate-300 leading-relaxed">
                            Mọi thông tin chỉnh sửa tại tab <strong>Thông Tin Lô Hàng</strong> sau khi nhấn <em>“Hoàn thành và cập nhật dữ liệu”</em> sẽ tự động quy chiếu và làm mới toàn bộ kết quả ở các phân hệ Báo giá, Biên lợi nhuận, Dự báo Space, Mùa cao điểm và Sàn Slot Marketplace.
                        </p>
                    </div>
                </div>
            </div>

            <!-- TAB 2: FORM NHẬP VÀ ĐIỀU CHỈNH THÔNG TIN LÔ HÀNG (PHÂN HỆ A) -->
            <div v-if="currentTab === 'shipmentForm'" class="space-y-6 w-full">
                <div class="bg-slate-800/80 border border-slate-700/80 rounded-2xl p-6 shadow-xl space-y-5 w-full">
                    <div class="flex justify-between items-center pb-3 border-b border-slate-700/60">
                        <h3 class="text-base font-bold text-blue-400 flex items-center gap-2">
                            <i class="fa-solid fa-pen-to-square"></i> Cấu Hình & Chỉnh Sửa Thông Tin Lô Hàng (Input Trung Tâm)
                        </h3>
                        <span class="text-xs text-slate-400">Nhập đầy đủ thông tin và bấm Hoàn thành để cập nhật đồng bộ</span>
                    </div>

                    <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-4 text-xs">
                        <!-- Nhóm 1: Các bên liên quan -->
                        <div class="space-y-3 bg-slate-900/50 p-3 rounded-xl border border-slate-700/50">
                            <div class="font-semibold text-slate-200 border-b border-slate-700 pb-1">1. Các Bên Liên Quan</div>
                            <div>
                                <label class="text-slate-400 block mb-1">Shipper</label>
                                <input type="text" v-model="tempShipment.shipper" class="w-full bg-slate-800 border border-slate-700 rounded-lg p-2 text-slate-100">
                            </div>
                            <div>
                                <label class="text-slate-400 block mb-1">Consignee</label>
                                <input type="text" v-model="tempShipment.consignee" class="w-full bg-slate-800 border border-slate-700 rounded-lg p-2 text-slate-100">
                            </div>
                            <div>
                                <label class="text-slate-400 block mb-1">Khách Hàng (Client)</label>
                                <input type="text" v-model="tempShipment.customer" class="w-full bg-slate-800 border border-slate-700 rounded-lg p-2 text-slate-100">
                            </div>
                            <div>
                                <label class="text-slate-400 block mb-1">Sales Phụ Trách</label>
                                <input type="text" v-model="tempShipment.salesPerson" class="w-full bg-slate-800 border border-slate-700 rounded-lg p-2 text-slate-100">
                            </div>
                        </div>

                        <!-- Nhóm 2: Tuyến & Cảng -->
                        <div class="space-y-3 bg-slate-900/50 p-3 rounded-xl border border-slate-700/50">
                            <div class="font-semibold text-slate-200 border-b border-slate-700 pb-1">2. Tuyến Vận Tải (POL / POD)</div>
                            <div>
                                <label class="text-slate-400 block mb-1">Cảng Đi (POL)</label>
                                <select v-model="tempShipment.pol" class="w-full bg-slate-800 border border-slate-700 rounded-lg p-2 text-slate-100">
                                    <option value="Cái Mép (VNVUT)">Cái Mép (VNVUT)</option>
                                    <option value="Cát Lái (VNCLI)">Cát Lái (VNCLI)</option>
                                    <option value="Hải Phòng (VNHPH)">Hải Phòng (VNHPH)</option>
                                    <option value="Đà Nẵng (VNDAN)">Đà Nẵng (VNDAN)</option>
                                    <option value="Shanghai (CNSHA)">Shanghai (CNSHA)</option>
                                </select>
                            </div>
                            <div>
                                <label class="text-slate-400 block mb-1">Cảng Đến (POD)</label>
                                <select v-model="tempShipment.pod" class="w-full bg-slate-800 border border-slate-700 rounded-lg p-2 text-slate-100">
                                    <option value="Los Angeles (USLAX)">Los Angeles (USLAX)</option>
                                    <option value="Long Beach (USLGB)">Long Beach (USLGB)</option>
                                    <option value="New York (USNYC)">New York (USNYC)</option>
                                    <option value="Hamburg (DEHAM)">Hamburg (DEHAM)</option>
                                    <option value="Rotterdam (NLRTM)">Rotterdam (NLRTM)</option>
                                </select>
                            </div>
                            <div>
                                <label class="text-slate-400 block mb-1">Loại Hàng Hóa (Commodity)</label>
                                <input type="text" v-model="tempShipment.commodity" class="w-full bg-slate-800 border border-slate-700 rounded-lg p-2 text-slate-100">
                            </div>
                        </div>

                        <!-- Nhóm 3: Quy mô & Container -->
                        <div class="space-y-3 bg-slate-900/50 p-3 rounded-xl border border-slate-700/50">
                            <div class="font-semibold text-slate-200 border-b border-slate-700 pb-1">3. Quy Mô & Container</div>
                            <div class="grid grid-cols-2 gap-2">
                                <div>
                                    <label class="text-slate-400 block mb-1">Loại Container</label>
                                    <select v-model="tempShipment.containerType" class="w-full bg-slate-800 border border-slate-700 rounded-lg p-2 text-slate-100">
                                        <option value="20'GP">20'GP</option>
                                        <option value="40'GP">40'GP</option>
                                        <option value="40'HC">40'HC</option>
                                        <option value="45'HC">45'HC</option>
                                        <option value="Reefer">Reefer 40'</option>
                                    </select>
                                </div>
                                <div>
                                    <label class="text-slate-400 block mb-1">Số Lượng Cont</label>
                                    <input type="number" min="1" max="100" v-model.number="tempShipment.volume" class="w-full bg-slate-800 border border-slate-700 rounded-lg p-2 text-amber-400 font-bold">
                                </div>
                            </div>
                            <div>
                                <label class="text-slate-400 block mb-1">Hãng Tàu Ưu Tiên</label>
                                <select v-model="tempShipment.preferredCarrier" class="w-full bg-slate-800 border border-slate-700 rounded-lg p-2 text-slate-100">
                                    <option value="Wan Hai Lines">Wan Hai Lines</option>
                                    <option value="Evergreen Line">Evergreen Line</option>
                                    <option value="COSCO Shipping">COSCO Shipping</option>
                                </select>
                            </div>
                            <div>
                                <label class="text-slate-400 block mb-1">Mục tiêu Biên Lãi (%)</label>
                                <input type="number" min="1" max="50" v-model.number="targetMargin" class="w-full bg-slate-800 border border-slate-700 rounded-lg p-2 text-blue-400 font-bold">
                            </div>
                        </div>

                        <!-- Nhóm 4: Lịch trình -->
                        <div class="space-y-3 bg-slate-900/50 p-3 rounded-xl border border-slate-700/50">
                            <div class="font-semibold text-slate-200 border-b border-slate-700 pb-1">4. Lịch Trình (ETD / ETA)</div>
                            <div>
                                <label class="text-slate-400 block mb-1">Ngày Hàng Sẵn (CRD)</label>
                                <input type="date" v-model="tempShipment.crd" class="w-full bg-slate-800 border border-slate-700 rounded-lg p-2 text-slate-100">
                            </div>
                            <div>
                                <label class="text-slate-400 block mb-1">ETD Dự Kiến</label>
                                <input type="date" v-model="tempShipment.etd" class="w-full bg-slate-800 border border-slate-700 rounded-lg p-2 text-slate-100">
                            </div>
                            <div>
                                <label class="text-slate-400 block mb-1">ETA Dự Kiến</label>
                                <input type="date" v-model="tempShipment.eta" class="w-full bg-slate-800 border border-slate-700 rounded-lg p-2 text-slate-100">
                            </div>
                        </div>
                    </div>

                    <!-- Nút xác nhận bắt buộc -->
                    <div class="pt-4 border-t border-slate-700 flex justify-end gap-3">
                        <button @click="commitShipmentUpdate" class="bg-blue-600 hover:bg-blue-500 text-white px-6 py-2.5 rounded-xl text-xs font-bold shadow-lg transition flex items-center gap-2">
                            <i class="fa-solid fa-check"></i> Hoàn Thành Và Cập Nhật Dữ Liệu
                        </button>
                    </div>
                </div>
            </div>

            <!-- TAB 3: BÁO GIÁ DỰ KIẾN & KIỂM SOÁT BIÊN LỢI NHUẬN (PHÂN HỆ B) -->
            <div v-if="currentTab === 'quotation'" class="space-y-6 w-full">
                <div class="bg-slate-800/80 border border-slate-700/80 rounded-2xl p-5 shadow-xl space-y-4 w-full">
                    <div class="flex justify-between items-center pb-3 border-b border-slate-700/60">
                        <h3 class="text-sm font-bold text-blue-400 flex items-center gap-2">
                            <i class="fa-solid fa-file-invoice-dollar"></i> Phân Hệ B: Kiểm Soát Biên Lợi Nhuận Gộp (Mục Tiêu {{ targetMargin }}%)
                        </h3>
                        <span class="text-xs text-slate-400">Đang áp dụng cho lô: <strong>{{ shipment.volume }} x {{ shipment.containerType }}</strong> ({{ shipment.pol }} → {{ shipment.pod }})</span>
                    </div>

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
                                    <span class="text-slate-400 block">Tổng Giá Vốn (1 Cont)</span>
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

                            <!-- Công thức Kiểm thử Biên Lợi Nhuận -->
                            <div class="pt-2 border-t border-slate-800 flex flex-col md:flex-row md:items-center justify-between gap-3 text-xs">
                                <div class="grid grid-cols-2 md:grid-cols-4 gap-6">
                                    <div>
                                        <span class="text-slate-400 block">Giá Bán Đề Xuất ($)</span>
                                        <input type="number" v-model.number="carrier.currentSellRate" class="w-28 bg-slate-800 border border-slate-700 rounded p-1 text-slate-100 font-bold mt-1">
                                    </div>
                                    <div>
                                        <span class="text-slate-400 block">Giá Bán Tối Thiểu (Chuẩn {{ targetMargin }}%)</span>
                                        <span class="font-bold text-emerald-400 text-sm">${{ carrier.minSellRateRequired }} USD</span>
                                    </div>
                                    <div>
                                        <span class="text-slate-400 block">Biên Lợi Nhuận Gộp</span>
                                        <span class="font-bold" :class="carrier.marginPercent >= targetMargin ? 'text-emerald-400' : 'text-amber-400'">
                                            {{ carrier.marginPercent }}%
                                        </span>
                                    </div>
                                    <div>
                                        <span class="text-slate-400 block">Tổng Lãi Toàn Lô ({{ shipment.volume }} cont)</span>
                                        <span class="font-bold" :class="carrier.totalProfit >= 0 ? 'text-emerald-400' : 'text-rose-400'">${{ carrier.totalProfit.toLocaleString() }} USD</span>
                                    </div>
                                </div>

                                <div>
                                    <span v-if="carrier.marginPercent < targetMargin" class="px-3 py-1.5 rounded-lg bg-rose-500/20 text-rose-300 border border-rose-500/30 text-xs font-semibold flex items-center gap-1.5">
                                        <i class="fa-solid fa-triangle-exclamation"></i> Chưa đạt chuẩn biên lãi {{ targetMargin }}%
                                    </span>
                                    <span v-else class="px-3 py-1.5 rounded-lg bg-emerald-500/20 text-emerald-300 border border-emerald-500/30 text-xs font-semibold flex items-center gap-1.5">
                                        <i class="fa-solid fa-circle-check"></i> Đạt chuẩn biên lãi
                                    </span>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>

            <!-- TAB 4: DỰ BÁO SPACE (PHÂN HỆ C) -->
            <div v-if="currentTab === 'spaceForecast'" class="space-y-6 w-full">
                <div class="bg-slate-800/80 border border-slate-700/80 rounded-2xl p-5 shadow-xl space-y-4 w-full">
                    <h3 class="text-sm font-bold text-amber-400 flex items-center gap-2">
                        <i class="fa-solid fa-shield-halved"></i> Phân Hệ C: Theo Dõi Cung Cầu Space & Thiếu Hụt Theo Tuyến (Đã đồng bộ)
                    </h3>

                    <div class="grid grid-cols-1 md:grid-cols-3 gap-4 text-xs">
                        <div class="bg-slate-900/70 p-4 rounded-xl border border-slate-700 space-y-2">
                            <div class="font-semibold text-slate-200">Cân Đối Cung Cầu Tuyến: {{ shipment.pol }} → {{ shipment.pod }}</div>
                            <div>Nhu cầu đặt chỗ: <strong class="text-white">{{ shipment.volume }} containers ({{ shipment.containerType }})</strong></div>
                            <div>Nguồn cung khả dụng (Available): <strong class="text-amber-400">{{ availableAllocatedSpace }} containers</strong></div>
                            <div class="pt-2 border-t border-slate-800">
                                Mức thiếu hụt space: <strong :class="spaceDeficit > 0 ? 'text-rose-400 text-sm' : 'text-emerald-400 text-sm'">{{ spaceDeficit }} Containers</strong>
                            </div>
                        </div>

                        <div class="md:col-span-2 bg-gradient-to-br from-amber-500/10 to-orange-500/10 p-4 rounded-xl border border-amber-500/30 space-y-2">
                            <div class="font-bold text-amber-400 text-sm"><i class="fa-solid fa-triangle-exclamation mr-1"></i> Đánh Giá Rủi Ro Space (Rule-based Assessment)</div>
                            <p class="text-xs text-slate-300 leading-relaxed">
                                Dựa trên ETD mục tiêu <strong>{{ shipment.etd }}</strong> và quy mô <strong>{{ shipment.volume }} container</strong>, hệ thống đã lọc lại dữ liệu và xác định mức độ rủi ro thiếu hụt theo thời gian thực.
                            </p>
                            <div class="text-[11px] text-slate-400 italic">Khuyến nghị: Kết hợp tìm kiếm slot bù đắp tại Sàn Slot Marketplace.</div>
                        </div>
                    </div>
                </div>
            </div>

            <!-- TAB 5: MÙA CAO ĐIỂM & ĐẶT BOOKING (PHÂN HỆ D) -->
            <div v-if="currentTab === 'peakSeason'" class="space-y-6 w-full">
                <div class="bg-slate-800/80 border border-slate-700/80 rounded-2xl p-5 shadow-xl space-y-4 w-full">
                    <h3 class="text-sm font-bold text-amber-400 flex items-center gap-2">
                        <i class="fa-solid fa-calendar-days"></i> Phân Hệ D: Nhận Diện Mùa Cao Điểm & Mốc Đặt Booking Khuyến Nghị
                    </h3>

                    <div class="grid grid-cols-1 md:grid-cols-2 gap-4 text-xs">
                        <div class="bg-slate-900/70 p-4 rounded-xl border border-slate-700 space-y-2">
                            <div class="font-bold text-white text-sm">Bối Cảnh Thị Trường Tuyến Chọn</div>
                            <p class="text-slate-300"><strong>Tuyến:</strong> {{ shipment.pol }} → {{ shipment.pod }}</p>
                            <p class="text-slate-300"><strong>ETD Lô Hàng:</strong> {{ shipment.etd }}</p>
                            <p class="text-slate-300"><strong>Nhận định:</strong> Nằm trong khung thời điểm thị trường chịu áp lực cung ứng, cần tuân thủ nghiêm ngặt mốc đặt chỗ sớm.</p>
                        </div>

                        <div class="bg-slate-900/70 p-4 rounded-xl border border-slate-700 space-y-2">
                            <div class="font-bold text-emerald-400 text-sm">Mốc Thời Gian Đặt Booking (Tính Ngược Từ ETD {{ shipment.etd }})</div>
                            <p class="text-slate-300">• Thời điểm hỏi giá: <strong class="text-white">Trước ETD 28 ngày</strong></p>
                            <p class="text-slate-300">• Thời điểm kiểm tra & giữ chỗ: <strong class="text-white">Trước ETD 21 ngày</strong></p>
                            <p class="text-slate-300">• Ngày hoàn tất booking chuẩn: <strong class="text-emerald-400">Trước ETD 14 ngày</strong></p>
                        </div>
                    </div>
                </div>
            </div>

            <!-- TAB 6: SÀN GIAO DỊCH SLOT SPACE (PHÂN HỆ E) -->
            <div v-if="currentTab === 'marketplace'" class="space-y-6 w-full">
                <div class="bg-slate-800/80 border border-slate-700/80 rounded-2xl p-5 shadow-xl space-y-4 w-full">
                    <div class="flex justify-between items-center pb-3 border-b border-slate-700/60">
                        <h3 class="text-sm font-bold text-emerald-400 flex items-center gap-2">
                            <i class="fa-solid fa-right-left"></i> Phân Hệ E: Sàn Giao Dịch Slot Space (DEMO Marketplace)
                        </h3>
                        <span class="text-xs text-slate-400">Đã lọc theo tuyến: <strong>{{ shipment.pol }} → {{ shipment.pod }}</strong></span>
                    </div>

                    <div class="grid grid-cols-1 md:grid-cols-2 gap-4 w-full">
                        <div v-for="slot in filteredMarketplaceList" :key="slot.id" class="bg-slate-900/70 border border-slate-700/80 rounded-xl p-4 flex flex-col justify-between gap-3 text-xs">
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
                                <button @click="claimMarketplaceSlot(slot)" class="bg-emerald-600 hover:bg-emerald-500 text-white px-3 py-1.5 rounded-lg transition font-medium">
                                    Yêu Cầu Nhượng Slot (DEMO)
                                </button>
                            </div>
                        </div>
                    </div>
                </div>
            </div>

        </main>
    </div>

    <!-- Script Vue.js 3 Logic & Đồng Bộ State Toàn Diện -->
    <script>
        const { createApp } = Vue;

        createApp({
            data() {
                return {
                    currentTab: 'dashboard',
                    targetMargin: 10, // Mặc định chuẩn 10%
                    lastUpdatedTime: new Date().toLocaleTimeString(),

                    // State trung tâm chính thức sau khi xác nhận
                    shipment: {
                        shipper: 'QA Furniture Co., Ltd',
                        consignee: 'MTA Cabinets LLC',
                        customer: 'MTA Cabinets LLC',
                        salesPerson: 'Bắp (Sales)',
                        pol: 'Cái Mép (VNVUT)',
                        pod: 'Los Angeles (USLAX)',
                        commodity: 'Wooden kitchen cabinets',
                        containerType: "40'HC",
                        volume: 5,
                        preferredCarrier: 'Wan Hai Lines',
                        crd: '2026-05-28',
                        etd: '2026-06-08',
                        eta: '2026-06-30'
                    },

                    // State tạm thời trên Form chỉnh sửa
                    tempShipment: {
                        shipper: 'QA Furniture Co., Ltd',
                        consignee: 'MTA Cabinets LLC',
                        customer: 'MTA Cabinets LLC',
                        salesPerson: 'Bắp (Sales)',
                        pol: 'Cái Mép (VNVUT)',
                        pod: 'Los Angeles (USLAX)',
                        commodity: 'Wooden kitchen cabinets',
                        containerType: "40'HC",
                        volume: 5,
                        preferredCarrier: 'Wan Hai Lines',
                        crd: '2026-05-28',
                        etd: '2026-06-08',
                        eta: '2026-06-30'
                    },

                    carriers: [
                        {
                            id: 1,
                            name: 'Wan Hai Lines',
                            code: 'WHL',
                            vessel: 'WAN HAI A01 E012',
                            etd: '2026-06-10',
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
                            etd: '2026-06-09',
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
                        { id: 101, provider: 'VinaFreighter Logistics', carrier: 'Evergreen', route: 'Cái Mép (VNVUT) → Los Angeles (USLAX)', pol: 'Cái Mép (VNVUT)', pod: 'Los Angeles (USLAX)', etd: '2026-06-08', slots: 3, price: 5240 },
                        { id: 102, provider: 'Global Forwarding Partner', carrier: 'COSCO', route: 'Cái Mép (VNVUT) → Long Beach (USLGB)', pol: 'Cái Mép (VNVUT)', pod: 'Long Beach (USLGB)', etd: '2026-06-10', slots: 2, price: 5220 }
                    ]
                }
            },
            computed: {
                availableAllocatedSpace() {
                    const matched = this.carriers.find(c => c.name === this.shipment.preferredCarrier);
                    return matched ? matched.spaceAvailable : 3;
                },
                spaceDeficit() {
                    return Math.max(0, this.shipment.volume - this.availableAllocatedSpace);
                },
                evaluatedCarriers() {
                    return this.carriers.map(c => {
                        const totalCostPerCont = c.oceanFreight + c.pss + c.localCharges + c.extraSlotFee + c.reserveFee;
                        
                        // Công thức kiểm thử biên lợi nhuận chuẩn: Giá bán tối thiểu = Giá vốn / (1 - targetMargin%)
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
                },
                filteredMarketplaceList() {
                    // Lọc tin đăng slot theo POL hiện tại của shipment
                    return this.marketplaceList.filter(slot => slot.pol === this.shipment.pol || slot.route.includes(this.shipment.pol.split(' ')[0]));
                }
            },
            methods: {
                commitShipmentUpdate() {
                    // Kiểm tra tính hợp lệ dữ liệu cơ bản theo yêu cầu
                    if (!this.tempShipment.volume || this.tempShipment.volume <= 0) {
                        alert('Lỗi: Số lượng container phải là số lớn hơn 0!');
                        return;
                    }
                    if (this.tempShipment.eta < this.tempShipment.etd) {
                        alert('Cảnh báo: Ngày ETA không thể trước ngày ETD. Vui lòng kiểm tra lại lịch trình!');
                        return;
                    }

                    // Đồng bộ dữ liệu tạm sang state chính thức
                    this.shipment = JSON.parse(JSON.stringify(this.tempShipment));
                    this.lastUpdatedTime = new Date().toLocaleTimeString();

                    alert(`Đã hoàn thành và cập nhật dữ liệu lô hàng thành công! Tất cả phân hệ Báo giá, Lợi nhuận, Dự báo Space và Sàn Slot đã được đồng bộ theo tuyến ${this.shipment.pol} → ${this.shipment.pod} (${this.shipment.volume} cont).`);
                    this.currentTab = 'quotation';
                },
                resetToDefault() {
                    this.targetMargin = 10;
                    this.shipment = {
                        shipper: 'QA Furniture Co., Ltd',
                        consignee: 'MTA Cabinets LLC',
                        customer: 'MTA Cabinets LLC',
                        salesPerson: 'Bắp (Sales)',
                        pol: 'Cái Mép (VNVUT)',
                        pod: 'Los Angeles (USLAX)',
                        commodity: 'Wooden kitchen cabinets',
                        containerType: "40'HC",
                        volume: 5,
                        preferredCarrier: 'Wan Hai Lines',
                        crd: '2026-05-28',
                        etd: '2026-06-08',
                        eta: '2026-06-30'
                    };
                    this.tempShipment = JSON.parse(JSON.stringify(this.shipment));
                    this.lastUpdatedTime = new Date().toLocaleTimeString();
                    alert('Đã đặt lại dữ liệu mẫu kiểm thử tiêu chuẩn.');
                },
                claimMarketplaceSlot(slot) {
                    if (slot.slots <= 0) {
                        alert('Tin đăng đã hết slot khả dụng!');
                        return;
                    }
                    alert(`Đã gửi yêu cầu giữ chỗ thành công cho ${slot.slots} slot từ ${slot.provider} (Thao tác DEMO Marketplace)!`);
                }
            }
        }).mount('#app');
    </script>
</body>
</html>
"""

# Render hiển thị giao diện toàn màn hình trong Streamlit
st.components.v1.html(html_code, height=980, scrolling=True)
