import streamlit as st

# Cấu hình trang Streamlit
st.set_page_config(
    page_title="LogiSpace Simulator - Quản Lý Báo Giá & Dự Báo Space",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Khối mã HTML/JS hoàn chỉnh được bao bọc an toàn bằng dấu nháy ba (""")
html_code = """
<!DOCTYPE html>
<html lang="vi">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>LogiSpace Predict & Simulation Platform</title>
    <!-- Tailwind CSS CDN -->
    <script src="https://cdn.tailwindcss.com"></script>
    <!-- FontAwesome Icons CDN -->
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <!-- Vue.js 3 CDN -->
    <script src="https://unpkg.com/vue@3/dist/vue.global.js"></script>
</head>
<body class="bg-slate-900 text-slate-100 font-sans min-h-screen">

    <div id="app" class="flex flex-col min-h-screen">
        <!-- Header -->
        <header class="border-b border-slate-800 bg-slate-950/80 backdrop-blur sticky top-0 z-50">
            <div class="max-w-7xl mx-auto px-4 py-3 flex justify-between items-center">
                <div class="flex items-center gap-3">
                    <div class="bg-blue-600 text-white p-2 rounded-lg font-bold">
                        <i class="fa-solid fa-sliders"></i>
                    </div>
                    <div>
                        <h1 class="font-bold text-lg leading-none text-blue-400">LogiSpace Simulator</h1>
                        <span class="text-xs text-slate-400">Hệ Thống Mô Phỏng & Dự Báo Space Linh Hoạt</span>
                    </div>
                </div>
                
                <div class="flex items-center gap-4">
                    <span class="text-xs px-2.5 py-1 rounded-full bg-blue-500/10 text-blue-400 border border-blue-500/20 flex items-center gap-1.5">
                        <i class="fa-solid fa-gear animate-spin"></i> Dynamic Simulation Engine Active
                    </span>
                    <button @click="resetToDefaultCase" class="text-xs bg-slate-800 hover:bg-slate-700 text-slate-300 border border-slate-700 px-3 py-1.5 rounded-lg transition flex items-center gap-1.5">
                        <i class="fa-solid fa-rotate-left"></i> Reset Về Case Mẫu (QA Furniture)
                    </button>
                </div>
            </div>
        </header>

        <!-- Dynamic Control Bar & Main Area -->
        <main class="flex-1 max-w-7xl w-full mx-auto p-4 md:p-6 space-y-6">
            
            <!-- PANEL 1: BẢNG TÙY CHỈNH NỘI DUNG & SỐ LIỆU CASE STUDY (INPUT PARAMETERS) -->
            <div class="bg-slate-800/80 border border-blue-500/30 rounded-xl p-5 shadow-xl">
                <div class="flex items-center justify-between mb-4 pb-2 border-b border-slate-700">
                    <h2 class="text-base font-bold text-blue-400 flex items-center gap-2">
                        <i class="fa-solid fa-pen-to-square"></i> Bảng Điều Chỉnh Thông Số & Số Liệu Case Study
                    </h2>
                    <span class="text-xs text-slate-400">Chỉnh sửa số liệu bên dưới để chạy mô phỏng mới</span>
                </div>

                <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-4 text-xs">
                    
                    <!-- Nhóm 1: Thông tin tuyến & hàng hóa -->
                    <div class="space-y-2 bg-slate-900/60 p-3 rounded-lg border border-slate-700/50">
                        <div class="font-semibold text-slate-200 border-b border-slate-800 pb-1">1. Hành Trình & Quy Mô</div>
                        <div>
                            <label class="text-slate-400 block">Shipper / Khách hàng</label>
                            <input type="text" v-model="sim.shipper" class="w-full bg-slate-800 border border-slate-700 rounded p-1.5 text-slate-100 focus:border-blue-500">
                        </div>
                        <div class="grid grid-cols-2 gap-2">
                            <div>
                                <label class="text-slate-400 block">Cảng Đi (POL)</label>
                                <select v-model="sim.pol" class="w-full bg-slate-800 border border-slate-700 rounded p-1.5 text-slate-100">
                                    <option value="Cái Mép (VNVUT)">Cái Mép (VNVUT)</option>
                                    <option value="Cát Lái (VNCLI)">Cát Lái (VNCLI)</option>
                                    <option value="Hải Phòng (VNHPH)">Hải Phòng (VNHPH)</option>
                                    <option value="Đà Nẵng (VNDAN)">Đà Nẵng (VNDAN)</option>
                                </select>
                            </div>
                            <div>
                                <label class="text-slate-400 block">Cảng Đến (POD)</label>
                                <select v-model="sim.pod" class="w-full bg-slate-800 border border-slate-700 rounded p-1.5 text-slate-100">
                                    <option value="Los Angeles (USLAX)">Los Angeles (USLAX)</option>
                                    <option value="Long Beach (USLGB)">Long Beach (USLGB)</option>
                                    <option value="New York (USNYC)">New York (USNYC)</option>
                                    <option value="Hamburg (DEHAM)">Hamburg (DEHAM)</option>
                                </select>
                            </div>
                        </div>
                        <div class="grid grid-cols-2 gap-2">
                            <div>
                                <label class="text-slate-400 block">Số Lượng Cont</label>
                                <input type="number" min="1" max="100" v-model.number="sim.volume" class="w-full bg-slate-800 border border-slate-700 rounded p-1.5 text-amber-400 font-bold">
                            </div>
                            <div>
                                <label class="text-slate-400 block">Loại Cont</label>
                                <select v-model="sim.containerType" class="w-full bg-slate-800 border border-slate-700 rounded p-1.5 text-slate-100">
                                    <option value="40'HC">40'HC</option>
                                    <option value="20'GP">20'GP</option>
                                    <option value="40'GP">40'GP</option>
                                    <option value="45'HC">45'HC</option>
                                </select>
                            </div>
                        </div>
                    </div>

                    <!-- Nhóm 2: Thời gian & Mùa vụ -->
                    <div class="space-y-2 bg-slate-900/60 p-3 rounded-lg border border-slate-700/50">
                        <div class="font-semibold text-slate-200 border-b border-slate-800 pb-1">2. Thời Gian & Yếu Tố Thị Trường</div>
                        <div>
                            <label class="text-slate-400 block">Tháng Xuất Hàng Dự Kiến</label>
                            <select v-model="sim.month" class="w-full bg-slate-800 border border-slate-700 rounded p-1.5 text-slate-100">
                                <option value="5">Tháng 5 (Cao điểm Chạy thuế)</option>
                                <option value="6">Tháng 6 (Cuối đợt Chạy thuế)</option>
                                <option value="8">Tháng 8 (Cao điểm Mùa Lễ Hội)</option>
                                <option value="10">Tháng 10 (Thấp điểm)</option>
                            </select>
                        </div>
                        <div>
                            <label class="text-slate-400 block">Ngày Book Lịch (Booking Date)</label>
                            <input type="date" v-model="sim.bookingDate" class="w-full bg-slate-800 border border-slate-700 rounded p-1.5 text-slate-100">
                        </div>
                        <div>
                            <label class="text-slate-400 block">Mức Độ Tải Thị Trường (Market Demand)</label>
                            <select v-model="sim.marketPressure" class="w-full bg-slate-800 border border-slate-700 rounded p-1.5 text-slate-100">
                                <option value="High">Rất Căng Thẳng (Thiếu Space Nặng)</option>
                                <option value="Medium">Trung Bình (Space Vừa Đủ)</option>
                                <option value="Low">Thấp (Dư Thừa Space)</option>
                            </select>
                        </div>
                    </div>

                    <!-- Nhóm 3: Chi phí & Cước phí -->
                    <div class="space-y-2 bg-slate-900/60 p-3 rounded-lg border border-slate-700/50">
                        <div class="font-semibold text-slate-200 border-b border-slate-800 pb-1">3. Khung Chi Phí & Báo Giá ($)</div>
                        <div class="grid grid-cols-2 gap-2">
                            <div>
                                <label class="text-slate-400 block">Cước Bán ($/Cont)</label>
                                <input type="number" v-model.number="sim.sellRate" class="w-full bg-slate-800 border border-slate-700 rounded p-1.5 text-emerald-400 font-bold">
                            </div>
                            <div>
                                <label class="text-slate-400 block">Cước Mua Gốc ($)</label>
                                <input type="number" v-model.number="sim.buyRate" class="w-full bg-slate-800 border border-slate-700 rounded p-1.5 text-blue-400 font-bold">
                            </div>
                        </div>
                        <div>
                            <label class="text-slate-400 block">Chi Phí Đổi Tàu/Lưu Kho Phát Sinh ($/Cont)</label>
                            <input type="number" v-model.number="sim.extraCost" class="w-full bg-slate-800 border border-slate-700 rounded p-1.5 text-rose-300">
                        </div>
                        <div>
                            <label class="text-slate-400 block">Phụ Phí Mùa Cao Điểm PSS ($/Cont)</label>
                            <input type="number" v-model.number="sim.pssSurcharge" class="w-full bg-slate-800 border border-slate-700 rounded p-1.5 text-amber-300">
                        </div>
                    </div>

                    <!-- Nhóm 4: Bảng Tổng Hợp Kết Quả Mô Phỏng Lợi Nhuận -->
                    <div class="bg-slate-900/90 p-3 rounded-lg border border-slate-700/80 flex flex-col justify-between">
                        <div>
                            <div class="font-semibold text-slate-200 border-b border-slate-800 pb-1 mb-2">4. Lợi Nhuận Mô Phỏng</div>
                            <div class="space-y-1">
                                <div class="flex justify-between">
                                    <span class="text-slate-400">Lãi gộp 1 Cont:</span>
                                    <span :class="profitPerCont >= 0 ? 'text-emerald-400 font-bold' : 'text-rose-400 font-bold'">${{ profitPerCont }} USD</span>
                                </div>
                                <div class="flex justify-between">
                                    <span class="text-slate-400">Tổng Lãi Toàn Lô ({{ sim.volume }} Cont):</span>
                                    <span :class="totalProfit >= 0 ? 'text-emerald-400 font-bold' : 'text-rose-400 font-bold'">${{ totalProfit }} USD</span>
                                </div>
                                <div class="flex justify-between text-[11px]">
                                    <span class="text-slate-400">Biên Lợi Nhuận:</span>
                                    <span class="text-slate-200 font-semibold">{{ marginPercent }}%</span>
                                </div>
                            </div>
                        </div>

                        <div v-if="profitPerCont <= 0" class="mt-2 p-2 bg-rose-500/20 border border-rose-500/30 rounded text-[10px] text-rose-300 leading-tight">
                            <i class="fa-solid fa-triangle-exclamation mr-1"></i> <strong>CẢNH BÁO LỖ:</strong> Chi phí phát sinh quá cao đè bẹp biên lợi nhuận lô hàng!
                        </div>
                        <div v-else class="mt-2 p-2 bg-emerald-500/20 border border-emerald-500/30 rounded text-[10px] text-emerald-300 leading-tight">
                            <i class="fa-solid fa-circle-check mr-1"></i> Lô hàng an toàn về mặt biên lợi nhuận.
                        </div>
                    </div>

                </div>
            </div>

            <!-- PANEL 2: DASHBOARD HIỂN THỊ DỰ BÁO VÀ KẾT QUẢ ĐIỀU CHỈNH -->
            <div class="grid grid-cols-1 lg:grid-cols-3 gap-6">
                
                <!-- Cột trái: AI Space Forecaster Cập Nhật Theo Tham Số -->
                <div class="lg:col-span-1 space-y-6">
                    
                    <!-- AI Forecast Card -->
                    <div class="bg-gradient-to-br from-amber-500/10 to-orange-500/10 border border-amber-500/30 rounded-xl p-5">
                        <div class="flex items-start justify-between mb-2">
                            <span class="text-xs font-semibold px-2 py-0.5 rounded bg-amber-500/20 text-amber-300 border border-amber-500/30">
                                <i class="fa-solid fa-robot mr-1"></i> AI Space Predictor
                            </span>
                            <span class="text-xs text-slate-400">{{ sim.pol }} -> {{ sim.pod }}</span>
                        </div>

                        <div class="text-xl font-bold mb-1" :class="aiCalculatedRisk > 70 ? 'text-rose-400' : (aiCalculatedRisk > 40 ? 'text-amber-400' : 'text-emerald-400')">
                            Mức Độ Thiếu Space: {{ aiCalculatedRisk }}% ({{ aiRiskLevelText }})
                        </div>

                        <p class="text-xs text-slate-300 leading-relaxed mb-3">
                            Dựa trên số liệu cài đặt: Yêu cầu <strong>{{ sim.volume }} x {{ sim.containerType }}</strong> trong tháng {{ sim.month }} với áp lực thị trường ở mức <strong>{{ sim.marketPressure }}</strong>.
                        </p>

                        <div class="w-full bg-slate-800 rounded-full h-2 overflow-hidden mb-2">
                            <div class="h-full transition-all duration-500" :style="{ width: aiCalculatedRisk + '%' }" :class="aiCalculatedRisk > 70 ? 'bg-rose-500' : (aiCalculatedRisk > 40 ? 'bg-amber-500' : 'bg-emerald-500')"></div>
                        </div>
                        <div class="text-[11px] text-slate-400 italic">
                            Khuyên dùng: {{ aiAdviceText }}
                        </div>
                    </div>

                    <!-- Lô Hàng Khách Hàng Card -->
                    <div class="bg-slate-800/60 border border-slate-700/60 rounded-xl p-5">
                        <h3 class="text-xs font-semibold text-slate-400 uppercase tracking-wider mb-2">Thông Tin Lô Hàng Mô Phỏng</h3>
                        <div class="text-xs space-y-1.5 text-slate-300">
                            <div><strong class="text-slate-400">Shipper:</strong> {{ sim.shipper }}</div>
                            <div><strong class="text-slate-400">Tuyến:</strong> {{ sim.pol }} -> {{ sim.pod }}</div>
                            <div><strong class="text-slate-400">Quy mô:</strong> <span class="text-amber-400 font-bold">{{ sim.volume }} x {{ sim.containerType }}</span></div>
                            <div><strong class="text-slate-400">Ngày Book:</strong> {{ sim.bookingDate }}</div>
                        </div>
                    </div>

                </div>

                <!-- Cột giữa & phải: Bảng So Sánh Hãng Tàu & Sàn Giao Dịch Slot -->
                <div class="lg:col-span-2 space-y-6">
                    
                    <!-- Tab Chuyển Đổi -->
                    <div class="flex border-b border-slate-800">
                        <button @click="activeTab = 'carriers'" :class="activeTab === 'carriers' ? 'border-blue-500 text-blue-400' : 'border-transparent text-slate-400 hover:text-slate-200'" class="px-4 py-2 border-b-2 font-medium text-sm transition">
                            <i class="fa-solid fa-ship mr-1.5"></i> Dự Báo Space Các Hãng Tàu
                        </button>
                        <button @click="activeTab = 'marketplace'" :class="activeTab === 'marketplace' ? 'border-blue-500 text-blue-400' : 'border-transparent text-slate-400 hover:text-slate-200'" class="px-4 py-2 border-b-2 font-medium text-sm transition">
                            <i class="fa-solid fa-right-left mr-1.5"></i> Sàn Slot Space Dự Phòng
                        </button>
                    </div>

                    <!-- TAB 1: Danh Sách Hãng Tàu Tính Toán Theo Quy Mô Cont Đã Nhập -->
                    <div v-if="activeTab === 'carriers'" class="space-y-4">
                        <div v-for="carrier in dynamicCarriers" :key="carrier.id" class="bg-slate-800/40 border border-slate-700/60 rounded-xl p-5 hover:border-slate-600 transition">
                            <div class="flex flex-col md:flex-row md:items-center justify-between gap-4">
                                
                                <div class="flex items-center gap-4">
                                    <div class="w-12 h-12 rounded-lg bg-slate-700 flex items-center justify-center text-lg font-bold text-slate-200 border border-slate-600">
                                        {{ carrier.code }}
                                    </div>
                                    <div>
                                        <div class="font-semibold text-slate-100 flex items-center gap-2">
                                            {{ carrier.name }}
                                        </div>
                                        <div class="text-xs text-slate-400 mt-1">
                                            Chuyến: <span class="text-slate-200 font-medium">{{ carrier.vessel }}</span> | ETD: <span class="text-slate-200 font-medium">{{ carrier.etd }}</span>
                                        </div>
                                    </div>
                                </div>

                                <div class="grid grid-cols-2 gap-4 text-left md:text-right border-t md:border-t-0 pt-3 md:pt-0 border-slate-700/50">
                                    <div>
                                        <div class="text-xs text-slate-400">Khả Năng Cung Cấp Space</div>
                                        <div class="text-sm font-semibold" :class="carrier.spaceAvailable >= sim.volume ? 'text-emerald-400' : 'text-amber-400'">
                                            {{ carrier.spaceAvailable }} / {{ sim.volume }} {{ sim.containerType }}
                                        </div>
                                    </div>
                                    <div>
                                        <div class="text-xs text-slate-400">Dự Báo Trễ Tàu (Roll-over)</div>
                                        <div class="text-sm font-semibold" :class="carrier.delayDays > 0 ? 'text-rose-400' : 'text-emerald-400'">
                                            {{ carrier.delayDays > 0 ? '+' + carrier.delayDays + ' Ngày' : 'Đúng Lịch' }}
                                        </div>
                                    </div>
                                </div>

                            </div>

                            <!-- Cước Mua & Thao Tác -->
                            <div class="mt-4 pt-3 border-t border-slate-700/40 flex flex-col md:flex-row md:items-center justify-between gap-3 bg-slate-900/40 -mx-5 -mb-5 p-4 rounded-b-xl">
                                <div class="text-xs">
                                    <span class="text-slate-400">Cước Mua Thực Tế (Bao gồm PSS):</span>
                                    <span class="text-base font-bold text-blue-400 ml-1.5">${{ carrier.finalBuyRate }} USD</span>
                                    <span class="text-slate-500"> / {{ sim.containerType }}</span>
                                </div>

                                <div class="flex items-center gap-2">
                                    <button v-if="carrier.spaceAvailable < sim.volume" @click="suggestSplitBatch(carrier)" class="bg-amber-600/30 hover:bg-amber-600/50 text-amber-200 border border-amber-500/40 text-xs font-semibold px-3 py-2 rounded-lg transition">
                                        <i class="fa-solid fa-scissors mr-1"></i> Tối Ưu Tách Lô
                                    </button>
                                    <button @click="openBookingModal(carrier)" class="bg-blue-600 hover:bg-blue-500 text-white text-xs font-semibold px-4 py-2 rounded-lg transition">
                                        <i class="fa-solid fa-check mr-1"></i> Đặt Space
                                    </button>
                                </div>
                            </div>
                        </div>
                    </div>

                    <!-- TAB 2: Sàn Slot Thứ Cấp Tự Động Cập Nhật Theo Số Cont Thiếu -->
                    <div v-if="activeTab === 'marketplace'" class="space-y-4">
                        <div class="bg-slate-800/40 border border-slate-700/60 rounded-xl p-4">
                            <p class="text-xs text-slate-300 leading-relaxed">
                                <i class="fa-solid fa-circle-info text-blue-400 mr-1"></i> Hệ thống đề xuất các Slot Space khả thi từ các Forwarder khác trùng với tuyến <strong>{{ sim.pol }} -> {{ sim.pod }}</strong>:
                            </p>
                        </div>

                        <div class="space-y-3">
                            <div v-for="item in dynamicMarketplaceSlots" :key="item.id" class="bg-slate-800/40 border border-slate-700/60 rounded-xl p-4 flex flex-col md:flex-row items-start md:items-center justify-between gap-4">
                                <div>
                                    <div class="flex items-center gap-2">
                                        <span class="text-xs font-semibold px-2 py-0.5 rounded bg-amber-500/10 text-amber-400 border border-amber-500/20">{{ item.seller }}</span>
                                        <span class="text-xs text-slate-400">Chuyến: {{ item.carrier }} (ETD: {{ item.etd }})</span>
                                    </div>
                                    <div class="text-sm font-medium text-slate-200 mt-1">
                                        {{ sim.pol }} -> {{ sim.pod }} | Khả dụng: {{ item.quantity }}x {{ sim.containerType }}
                                    </div>
                                </div>

                                <div class="flex items-center gap-4 w-full md:w-auto justify-between md:justify-end border-t md:border-t-0 pt-2 md:pt-0 border-slate-700">
                                    <div class="text-right">
                                        <div class="text-xs text-slate-400">Giá nhượng</div>
                                        <div class="text-sm font-bold text-emerald-400">${{ item.price }} USD/Cont</div>
                                    </div>
                                    <button @click="claimMarketplaceSlot(item)" class="bg-emerald-600 hover:bg-emerald-500 text-white text-xs font-semibold px-3 py-2 rounded-lg transition">
                                        Nhận Nhượng Slot
                                    </button>
                                </div>
                            </div>
                        </div>
                    </div>

                </div>

            </div>
        </main>

        <!-- Modal Xác Nhận Đặt Space -->
        <div v-if="showModal" class="fixed inset-0 bg-black/70 backdrop-blur-sm flex items-center justify-center p-4 z-50">
            <div class="bg-slate-800 border border-slate-700 rounded-xl p-6 max-w-md w-full space-y-4">
                <h3 class="text-lg font-bold text-slate-100 flex items-center gap-2">
                    <i class="fa-solid fa-circle-check text-emerald-400"></i> Xác Nhận Booking Mô Phỏng
                </h3>
                
                <div v-if="selectedCarrier" class="text-sm space-y-2 bg-slate-900 p-4 rounded-lg border border-slate-700/50 text-slate-300">
                    <div>Khách hàng: <strong class="text-white">{{ sim.shipper }}</strong></div>
                    <div>Hãng tàu: <strong class="text-white">{{ selectedCarrier.name }}</strong></div>
                    <div>Tuyến: <strong class="text-white">{{ sim.pol }} -> {{ sim.pod }}</strong></div>
                    <div>Quy mô: <strong class="text-amber-400">{{ sim.volume }} x {{ sim.containerType }}</strong></div>
                    <div>Tổng cước mua: <strong class="text-emerald-400">${{ selectedCarrier.finalBuyRate * sim.volume }} USD</strong></div>
                </div>

                <div class="flex justify-end gap-3 pt-2">
                    <button @click="showModal = false" class="px-4 py-2 bg-slate-700 hover:bg-slate-600 rounded-lg text-xs font-semibold transition">Đóng</button>
                    <button @click="confirmBooking" class="px-4 py-2 bg-blue-600 hover:bg-blue-500 text-white rounded-lg text-xs font-semibold transition">Xác Nhận Đặt Chỗ</button>
                </div>
            </div>
        </div>

    </div>

    <!-- Vue.js Application Logic -->
    <script>
        const { createApp } = Vue;

        createApp({
            data() {
                return {
                    activeTab: 'carriers',
                    showModal: false,
                    selectedCarrier: null,

                    // Bảng tham số mô phỏng linh hoạt (Simulation State)
                    sim: {
                        shipper: 'QA Furniture Co., Ltd',
                        pol: 'Cái Mép (VNVUT)',
                        pod: 'Los Angeles (USLAX)',
                        volume: 5,
                        containerType: "40'HC",
                        month: "5",
                        bookingDate: '2025-05-30',
                        marketPressure: 'High',
                        sellRate: 5438,
                        buyRate: 5230,
                        extraCost: 0,
                        pssSurcharge: 0
                    }
                }
            },
            computed: {
                // Tính toán lợi nhuận tài chính
                profitPerCont() {
                    return this.sim.sellRate - (this.sim.buyRate + this.sim.pssSurcharge) - this.sim.extraCost;
                },
                totalProfit() {
                    return this.profitPerCont * this.sim.volume;
                },
                marginPercent() {
                    if (!this.sim.sellRate) return 0;
                    return ((this.profitPerCont / this.sim.sellRate) * 100).toFixed(2);
                },

                // AI Tính toán tỷ lệ rủi ro Space tự động dựa trên tham số nhập vào
                aiCalculatedRisk() {
                    let baseRisk = 30;
                    if (this.sim.marketPressure === 'High') baseRisk += 40;
                    if (this.sim.marketPressure === 'Medium') baseRisk += 20;
                    if (this.sim.volume >= 5) baseRisk += 15;
                    if (this.sim.month === '5' || this.sim.month === '8') baseRisk += 10;
                    return Math.min(baseRisk, 98);
                },
                aiRiskLevelText() {
                    if (this.aiCalculatedRisk > 75) return "Cực Kỳ Căng Thẳng";
                    if (this.aiCalculatedRisk > 45) return "Trung Bình";
                    return "An Toàn";
                },
                aiAdviceText() {
                    if (this.aiCalculatedRisk > 75) return "Nên đặt chỗ trước ít nhất 14 ngày hoặc chia nhỏ lô hàng để ghép space.";
                    if (this.aiCalculatedRisk > 45) return "Nên xác nhận booking sớm trước 7 ngày.";
                    return "Space dồi dào, có thể đàm phán cước tốt hơn.";
                },

                // Danh sách Hãng Tàu tự động biến đổi theo Tham số
                dynamicCarriers() {
                    const finalBuy = this.sim.buyRate + this.sim.pssSurcharge;
                    
                    if (this.sim.marketPressure === 'High') {
                        return [
                            { id: 1, name: 'Wan Hai Lines', code: 'WHL', vessel: 'WAN HAI A01 E012', etd: '10/06/2025', delayDays: 2, spaceAvailable: Math.max(1, this.sim.volume - 2), finalBuyRate: finalBuy },
                            { id: 2, name: 'Evergreen Line', code: 'EMC', vessel: 'EVER GIVEN / 0421E', etd: '09/06/2025', delayDays: 0, spaceAvailable: this.sim.volume, finalBuyRate: finalBuy + 50 },
                            { id: 3, name: 'COSCO Shipping', code: 'COS', vessel: 'COSCO VIETNAM / 015E', etd: '12/06/2025', delayDays: 1, spaceAvailable: Math.max(2, this.sim.volume - 1), finalBuyRate: finalBuy + 20 }
                        ];
                    } else {
                        return [
                            { id: 1, name: 'Wan Hai Lines', code: 'WHL', vessel: 'WAN HAI A01 E012', etd: '08/06/2025', delayDays: 0, spaceAvailable: this.sim.volume + 5, finalBuyRate: finalBuy },
                            { id: 2, name: 'Evergreen Line', code: 'EMC', vessel: 'EVER GIVEN / 0421E', etd: '09/06/2025', delayDays: 0, spaceAvailable: this.sim.volume + 10, finalBuyRate: finalBuy - 30 },
                            { id: 3, name: 'COSCO Shipping', code: 'COS', vessel: 'COSCO VIETNAM / 015E', etd: '11/06/2025', delayDays: 0, spaceAvailable: this.sim.volume + 8, finalBuyRate: finalBuy - 10 }
                        ];
                    }
                },

                // Sàn Giao Dịch Slot Tự Động Biến Đổi Theo Tuyến & Cước Nhập Vào
                dynamicMarketplaceSlots() {
                    const basePrice = this.sim.buyRate;
                    return [
                        { id: 201, seller: 'VinaFreighter Corp', carrier: 'Evergreen', quantity: Math.ceil(this.sim.volume / 2), price: basePrice + 10, etd: 'Chuyến kế tiếp' },
                        { id: 202, seller: 'GEX Logistics', carrier: 'COSCO', quantity: this.sim.volume, price: basePrice - 20, etd: 'Tuần này' }
                    ];
                }
            },
            methods: {
                resetToDefaultCase() {
                    this.sim = {
                        shipper: 'QA Furniture Co., Ltd',
                        pol: 'Cái Mép (VNVUT)',
                        pod: 'Los Angeles (USLAX)',
                        volume: 5,
                        containerType: "40'HC",
                        month: "5",
                        bookingDate: '2025-05-30',
                        marketPressure: 'High',
                        sellRate: 5438,
                        buyRate: 5230,
                        extraCost: 0,
                        pssSurcharge: 0
                    };
                },
                openBookingModal(carrier) {
                    this.selectedCarrier = carrier;
                    this.showModal = true;
                },
                confirmBooking() {
                    alert(`Đã gửi yêu cầu Booking cho ${this.sim.volume}x ${this.sim.containerType} thành công!`);
                    this.showModal = false;
                },
                suggestSplitBatch(carrier) {
                    const missing = this.sim.volume - carrier.spaceAvailable;
                    alert(`GỢI Ý TÁCH LÔ: Hãng ${carrier.name} chỉ còn đáp ứng ${carrier.spaceAvailable} cont. Bạn nên đi trước ${carrier.spaceAvailable} cont và mua bổ sung ${missing} cont từ Sàn Slot Thứ Cấp.`);
                },
                claimMarketplaceSlot(item) {
                    alert(`Đã chốt nhận nhượng ${item.quantity} slot từ ${item.seller} với giá $${item.price}/cont!`);
                }
            }
        }).mount('#app');
    </script>
</body>
</html>
"""

# Hiển thị giao diện Web thông qua Streamlit Components
st.components.v1.html(html_code, height=900, scrolling=True)
