<!DOCTYPE html>
<html lang="vi">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>LogiSpace Simulator - Quản Lý Báo Giá & Dự Báo Space Mùa Cao Điểm</title>
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
        <header class="border-b border-slate-800 bg-slate-950/90 backdrop-blur sticky top-0 z-50">
            <div class="max-w-7xl mx-auto px-4 py-3 flex flex-col md:flex-row justify-between items-center gap-3">
                <div class="flex items-center gap-3">
                    <div class="bg-blue-600 text-white p-2.5 rounded-xl font-bold shadow-lg shadow-blue-600/30">
                        <i class="fa-solid fa-ship"></i>
                    </div>
                    <div>
                        <h1 class="font-bold text-lg leading-none text-blue-400">LogiSpace Simulator</h1>
                        <span class="text-xs text-slate-400">Hệ Thống Hỗ Trợ Sales Forwarding & Quản Trị Rủi Ro Space</span>
                    </div>
                </div>
                
                <div class="flex flex-wrap items-center gap-2">
                    <span class="text-xs px-2.5 py-1 rounded-full bg-amber-500/10 text-amber-400 border border-amber-500/30 flex items-center gap-1.5">
                        <i class="fa-solid fa-clock-rotate-left"></i> Case Lịch Sử: QA Furniture (Cái Mép $\rightarrow$ LAX)
                    </span>
                    <button @click="loadHistoricalCase" class="text-xs bg-slate-800 hover:bg-slate-700 text-slate-300 border border-slate-700 px-3 py-1.5 rounded-lg transition flex items-center gap-1.5">
                        <i class="fa-solid fa-rotate-left"></i> Nạp Case Mẫu
                    </button>
                    <button @click="exportDataJSON" class="text-xs bg-slate-800 hover:bg-slate-700 text-slate-300 border border-slate-700 px-3 py-1.5 rounded-lg transition flex items-center gap-1.5">
                        <i class="fa-solid fa-download"></i> Xuất JSON
                    </button>
                </div>
            </div>
        </header>

        <!-- Main Content -->
        <main class="flex-1 max-w-7xl w-full mx-auto p-4 md:p-6 space-y-6">
            
            <!-- MODULE 3: THÔNG TIN KHÁCH HÀNG & LÔ HÀNG -->
            <div class="bg-slate-800/80 border border-slate-700/80 rounded-2xl p-5 shadow-xl">
                <div class="flex flex-col md:flex-row md:items-center justify-between pb-3 mb-4 border-b border-slate-700/60 gap-2">
                    <h2 class="text-base font-bold text-blue-400 flex items-center gap-2">
                        <i class="fa-solid fa-file-invoice"></i> Module 3: Tiếp Nhận Thông Tin Lô Hàng & Yêu Cầu Báo Giá
                    </h2>
                    <div class="flex items-center gap-2 text-xs">
                        <span class="text-slate-400">Trạng thái dữ liệu:</span>
                        <span class="px-2 py-0.5 rounded bg-emerald-500/20 text-emerald-400 border border-emerald-500/30 font-medium">Đã kiểm định hợp lệ</span>
                    </div>
                </div>

                <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-4 text-xs">
                    <div class="space-y-3">
                        <div>
                            <label class="text-slate-400 block mb-1">Khách hàng / Shipper</label>
                            <input type="text" v-model="shipment.shipper" class="w-full bg-slate-900 border border-slate-700 rounded-lg p-2 text-slate-100">
                        </div>
                        <div>
                            <label class="text-slate-400 block mb-1">Mã Lô Hàng / RFQ ID</label>
                            <input type="text" v-model="shipment.rfqId" class="w-full bg-slate-900 border border-slate-700 rounded-lg p-2 text-blue-400 font-mono">
                        </div>
                        <div class="grid grid-cols-2 gap-2">
                            <div>
                                <label class="text-slate-400 block mb-1">POL (Cảng đi)</label>
                                <input type="text" v-model="shipment.pol" class="w-full bg-slate-900 border border-slate-700 rounded-lg p-2 text-slate-100">
                            </div>
                            <div>
                                <label class="text-slate-400 block mb-1">POD (Cảng đến)</label>
                                <input type="text" v-model="shipment.pod" class="w-full bg-slate-900 border border-slate-700 rounded-lg p-2 text-slate-100">
                            </div>
                        </div>
                    </div>

                    <div class="space-y-3">
                        <div class="grid grid-cols-2 gap-2">
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
                                <input type="number" min="1" max="100" v-model.number="shipment.volume" class="w-full bg-slate-900 border border-slate-700 rounded-lg p-2 text-amber-400 font-bold">
                            </div>
                        </div>
                        <div>
                            <label class="text-slate-400 block mb-1">Loại Hàng Hóa & Quy Mô</label>
                            <input type="text" v-model="shipment.cargoDesc" class="w-full bg-slate-900 border border-slate-700 rounded-lg p-2 text-slate-100">
                        </div>
                        <div class="grid grid-cols-2 gap-2">
                            <div>
                                <label class="text-slate-400 block mb-1">Ngày Hàng Sẵn (CRD)</label>
                                <input type="date" v-model="shipment.crd" class="w-full bg-slate-900 border border-slate-700 rounded-lg p-2 text-slate-100">
                            </div>
                            <div>
                                <label class="text-slate-400 block mb-1">ETD Mong Muốn</label>
                                <input type="date" v-model="shipment.etdDesired" class="w-full bg-slate-900 border border-slate-700 rounded-lg p-2 text-slate-100">
                            </div>
                        </div>
                    </div>

                    <div class="space-y-3">
                        <div class="grid grid-cols-2 gap-2">
                            <div>
                                <label class="text-slate-400 block mb-1">Chấp Nhận Chậm (Ngày)</label>
                                <input type="number" min="0" max="15" v-model.number="shipment.toleranceDays" class="w-full bg-slate-900 border border-slate-700 rounded-lg p-2 text-slate-100">
                            </div>
                            <div>
                                <label class="text-slate-400 block mb-1">Nhân Viên Phụ Trách</label>
                                <input type="text" v-model="shipment.salesPerson" class="w-full bg-slate-900 border border-slate-700 rounded-lg p-2 text-slate-100">
                            </div>
                        </div>
                        <div>
                            <label class="text-slate-400 block mb-1">Ghi Chú Nghiệp Vụ</label>
                            <input type="text" v-model="shipment.notes" class="w-full bg-slate-900 border border-slate-700 rounded-lg p-2 text-slate-100">
                        </div>
                        <div class="p-2 bg-slate-900/80 rounded-lg border border-slate-700/50 text-[11px] text-slate-300">
                            <i class="fa-solid fa-triangle-exclamation text-amber-400 mr-1"></i> <strong>Kiểm định:</strong> Số lượng {{ shipment.volume }} cont, tuyến {{ shipment.pol }} $\rightarrow$ {{ shipment.pod }}.
                        </div>
                    </div>

                    <!-- Báo Giá Bán Nhanh -->
                    <div class="bg-slate-900/90 rounded-xl p-3 border border-slate-700/80 flex flex-col justify-between">
                        <div>
                            <div class="font-semibold text-slate-200 border-b border-slate-800 pb-1 mb-2">Cấu Hình Giá Bán (Selling Rate)</div>
                            <div class="space-y-2">
                                <div>
                                    <label class="text-slate-400 block">Đơn Giá Bán ($/Cont)</label>
                                    <input type="number" v-model.number="pricing.sellRate" class="w-full bg-slate-800 border border-slate-700 rounded p-1.5 text-emerald-400 font-bold">
                                </div>
                                <div class="flex justify-between text-[11px]">
                                    <span class="text-slate-400">Tổng Doanh Thu:</span>
                                    <span class="text-slate-200 font-semibold">${{ totalRevenue.toLocaleString() }} USD</span>
                                </div>
                            </div>
                        </div>
                        <div class="text-[10px] text-slate-400 italic mt-2">
                            Hiệu lực báo giá: Đến ngày {{ pricing.validUntil }}
                        </div>
                    </div>
                </div>
            </div>

            <!-- DASHBOARD TỔNG QUAN & CẢNH BÁO RỦI RO (MODULE 9 & 3.2) -->
            <div class="grid grid-cols-1 lg:grid-cols-3 gap-6">
                <!-- Cột trái: Cảnh báo nghiệp vụ & Rủi ro Space -->
                <div class="space-y-6">
                    <div class="bg-slate-800/80 border border-slate-700/80 rounded-2xl p-5 shadow-xl space-y-4">
                        <h3 class="text-sm font-bold text-slate-200 flex items-center gap-2">
                            <i class="fa-solid fa-triangle-exclamation text-amber-400"></i> Cảnh Báo Nghiệp Vụ & Rủi Ro Space
                        </h3>

                        <div class="space-y-2.5 text-xs">
                            <div v-for="(warning, idx) in operationalWarnings" :key="idx" class="p-3 rounded-xl border flex items-start gap-2.5" :class="warning.type === 'danger' ? 'bg-rose-500/10 border-rose-500/30 text-rose-300' : 'bg-amber-500/10 border-amber-500/30 text-amber-300'">
                                <i :class="warning.type === 'danger' ? 'fa-solid fa-circle-xmark mt-0.5' : 'fa-solid fa-triangle-exclamation mt-0.5'"></i>
                                <div>
                                    <strong class="block text-white">{{ warning.title }}</strong>
                                    <span>{{ warning.desc }}</span>
                                </div>
                            </div>
                        </div>
                    </div>

                    <!-- AI / Rule-based Space Status -->
                    <div class="bg-gradient-to-br from-amber-500/10 to-orange-500/10 border border-amber-500/30 rounded-2xl p-5 shadow-xl">
                        <div class="flex justify-between items-center mb-2">
                            <span class="text-xs font-semibold px-2 py-0.5 rounded bg-amber-500/20 text-amber-300 border border-amber-500/30">
                                <i class="fa-solid fa-shield-halved mr-1"></i> Đánh Giá Rủi Ro Space
                            </span>
                            <span class="text-xs text-slate-400">Mùa Cao Điểm Front-loading</span>
                        </div>
                        <div class="text-xl font-bold text-amber-400 mb-1">Mức Độ Thiếu Space: Cao (85%)</div>
                        <p class="text-xs text-slate-300 leading-relaxed mb-3">
                            Yêu cầu <strong>{{ shipment.volume }} x {{ shipment.containerType }}</strong> trong giai đoạn thị trường căng thẳng. Nguy cơ rớt tàu (roll-over) cao nếu chọn hãng tàu không có cam kết allocation cố định.
                        </p>
                        <div class="w-full bg-slate-800 rounded-full h-2 overflow-hidden">
                            <div class="bg-amber-500 h-full w-[85%]"></div>
                        </div>
                    </div>
                </div>

                <!-- Cột phải: Module 7 & 4.3 - So Sánh Hãng Tàu, Giá Vốn & Lợi Nuận Chi Tiết -->
                <div class="lg:col-span-2 space-y-6">
                    <div class="bg-slate-800/80 border border-slate-700/80 rounded-2xl p-5 shadow-xl space-y-4">
                        <div class="flex flex-col md:flex-row md:items-center justify-between pb-3 border-b border-slate-700/60 gap-2">
                            <h3 class="text-sm font-bold text-blue-400 flex items-center gap-2">
                                <i class="fa-solid fa-scale-balanced"></i> Module 4 & 7: So Sánh Phương Án Hãng Tàu & Phân Tích Lợi Nhuận
                            </h3>
                            <div class="flex items-center gap-2 text-xs">
                                <span class="text-slate-400">Sắp xếp theo:</span>
                                <select v-model="sortBy" class="bg-slate-900 border border-slate-700 rounded-lg px-2 py-1 text-slate-200">
                                    <option value="profit">Lợi nhuận gộp cao nhất</option>
                                    <option value="space">Space khả dụng nhiều nhất</option>
                                    <option value="rate">Giá vốn thấp nhất</option>
                                </select>
                            </div>
                        </div>

                        <!-- Danh sách hãng tàu & phương án -->
                        <div class="space-y-4">
                            <div v-for="carrier in sortedCarriers" :key="carrier.id" class="bg-slate-900/60 border border-slate-700/60 rounded-xl p-4 hover:border-slate-600 transition space-y-3">
                                <div class="flex flex-col md:flex-row md:items-center justify-between gap-3">
                                    <div class="flex items-center gap-3">
                                        <div class="w-10 h-10 rounded-lg bg-slate-800 flex items-center justify-center font-bold text-slate-200 border border-slate-700">
                                            {{ carrier.code }}
                                        </div>
                                        <div>
                                            <div class="font-semibold text-slate-100 flex items-center gap-2">
                                                {{ carrier.name }}
                                                <span v-if="carrier.isCaseDefault" class="text-[10px] bg-amber-500/20 text-amber-300 px-2 py-0.5 rounded border border-amber-500/30">Case Lịch Sử</span>
                                            </div>
                                            <div class="text-xs text-slate-400">
                                                Tàu: <span class="text-slate-200 font-medium">{{ carrier.vessel }}</span> | ETD: <span class="text-slate-200 font-medium">{{ carrier.etd }}</span> | Trễ tàu: <span class="text-rose-400 font-semibold">+{{ carrier.delayDays }} ngày</span>
                                            </div>
                                        </div>
                                    </div>

                                    <div class="grid grid-cols-2 gap-4 text-left md:text-right text-xs">
                                        <div>
                                            <span class="text-slate-400 block">Space Khả Dụng</span>
                                            <span class="font-bold" :class="carrier.spaceAvailable >= shipment.volume ? 'text-emerald-400' : 'text-amber-400'">
                                                {{ carrier.spaceAvailable }} / {{ shipment.volume }} Cont
                                            </span>
                                        </div>
                                        <div>
                                            <span class="text-slate-400 block">Hiệu Lực Giá Mua</span>
                                            <span class="font-semibold" :class="carrier.priceValid ? 'text-emerald-400' : 'text-rose-400'">
                                                {{ carrier.priceValid ? 'Còn Hiệu Lực' : 'Đã Hết Hạn' }}
                                            </span>
                                        </div>
                                    </div>
                                </div>

                                <!-- Chi tiết thành phần chi phí (Module 4.3) -->
                                <div class="bg-slate-950/60 p-3 rounded-lg border border-slate-800/80 text-xs space-y-2">
                                    <div class="font-semibold text-slate-300 flex justify-between items-center">
                                        <span>Cấu Trúc Chi Phí Mua (1 Container):</span>
                                        <span class="text-blue-400 font-mono">Tổng Giá Vốn: ${{ carrier.totalBuyCost.toLocaleString() }} USD</span>
                                    </div>
                                    <div class="grid grid-cols-2 md:grid-cols-4 gap-2 text-[11px] text-slate-400">
                                        <div>Cước biển (O/F): <strong class="text-slate-200">${{ carrier.oceanFreight }}</strong></div>
                                        <div>Phụ phí PSS/GRI: <strong class="text-slate-200">${{ carrier.pss }}</strong></div>
                                        <div>Local Charges: <strong class="text-slate-200">${{ carrier.localCharges }}</strong></div>
                                        <div>Dự phòng rủi ro: <strong class="text-slate-200">${{ carrier.reserveCost }}</strong></div>
                                    </div>
                                </div>

                                <!-- Phân tích lợi nhuận tài chính (Module 5) -->
                                <div class="pt-2 border-t border-slate-800 flex flex-col md:flex-row md:items-center justify-between gap-3 text-xs">
                                    <div class="flex items-center gap-4">
                                        <div>
                                            <span class="text-slate-400">Lãi Gộp/Cont:</span>
                                            <span class="font-bold ml-1" :class="carrier.profitPerCont >= 0 ? 'text-emerald-400' : 'text-rose-400'">${{ carrier.profitPerCont }} USD</span>
                                        </div>
                                        <div>
                                            <span class="text-slate-400">Tổng Lãi Toàn Lô:</span>
                                            <span class="font-bold ml-1" :class="carrier.totalProfit >= 0 ? 'text-emerald-400' : 'text-rose-400'">${{ carrier.totalProfit.toLocaleString() }} USD</span>
                                        </div>
                                        <div>
                                            <span class="text-slate-400">Biên Lợi Nhuận:</span>
                                            <span class="font-semibold ml-1 text-slate-200">{{ carrier.marginPercent }}%</span>
                                        </div>
                                    </div>

                                    <div class="flex items-center gap-2">
                                        <button v-if="carrier.spaceAvailable < shipment.volume" @click="openSplitModal(carrier)" class="bg-amber-600/30 hover:bg-amber-600/50 text-amber-200 border border-amber-500/40 px-3 py-1.5 rounded-lg transition font-medium">
                                            <i class="fa-solid fa-scissors mr-1"></i> Phương Án Tách Lô
                                        </button>
                                        <button @click="openBookingModal(carrier)" class="bg-blue-600 hover:bg-blue-500 text-white px-4 py-1.5 rounded-lg transition font-medium">
                                            <i class="fa-solid fa-check mr-1"></i> Xác Nhận Booking Mô Phỏng
                                        </button>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>

            <!-- MODULE 8: SÀN SLOT DỰ PHÒNG & XỬ LÝ TÁCH LÔ -->
            <div class="bg-slate-800/80 border border-slate-700/80 rounded-2xl p-5 shadow-xl space-y-4">
                <div class="flex justify-between items-center pb-3 border-b border-slate-700/60">
                    <h3 class="text-sm font-bold text-emerald-400 flex items-center gap-2">
                        <i class="fa-solid fa-right-left"></i> Module 8: Sàn Slot Dự Phòng & Nguồn Cung Bổ Sung Thứ Cấp
                    </h3>
                    <span class="text-xs text-slate-400">Cứu nguy khi thiếu space mùa cao điểm</span>
                </div>

                <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
                    <div v-for="slot in secondarySlots" :key="slot.id" class="bg-slate-900/60 border border-slate-700/60 rounded-xl p-4 flex flex-col justify-between gap-3 text-xs">
                        <div class="flex justify-between items-start">
                            <div>
                                <span class="px-2 py-0.5 rounded bg-amber-500/10 text-amber-400 border border-amber-500/20 font-semibold">{{ slot.provider }}</span>
                                <div class="font-semibold text-slate-200 mt-1.5">Chuyến: {{ slot.carrier }} (ETD: {{ slot.etd }})</div>
                                <div class="text-slate-400">Tuyến: {{ shipment.pol }} $\rightarrow$ {{ shipment.pod }}</div>
                            </div>
                            <div class="text-right">
                                <div class="text-slate-400">Giá mua nhượng</div>
                                <div class="text-sm font-bold text-emerald-400">${{ slot.buyCost }} USD/Cont</div>
                            </div>
                        </div>

                        <div class="flex justify-between items-center pt-2 border-t border-slate-800">
                            <span class="text-slate-300">Khả dụng: <strong>{{ slot.availableSlots }} Slot {{ shipment.containerType }}</strong></span>
                            <button @click="claimSecondarySlot(slot)" class="bg-emerald-600 hover:bg-emerald-500 text-white px-3 py-1.5 rounded-lg transition font-medium">
                                Nhận Nhượng Slot Mô Phỏng
                            </button>
                        </div>
                    </div>
                </div>
            </div>

        </main>

        <!-- Modal Xác Nhận Booking Mô Phỏng -->
        <div v-if="showModal" class="fixed inset-0 bg-black/70 backdrop-blur-sm flex items-center justify-center p-4 z-50">
            <div class="bg-slate-800 border border-slate-700 rounded-2xl p-6 max-w-md w-full space-y-4 shadow-2xl">
                <h3 class="text-lg font-bold text-slate-100 flex items-center gap-2">
                    <i class="fa-solid fa-circle-check text-emerald-400"></i> Xác Nhận Booking Mô Phỏng (Simulation)
                </h3>
                
                <div v-if="selectedCarrier" class="text-sm space-y-2 bg-slate-900 p-4 rounded-lg border border-slate-700/50 text-slate-300">
                    <div>Khách hàng: <strong class="text-white">{{ shipment.shipper }}</strong></div>
                    <div>Hãng tàu: <strong class="text-white">{{ selectedCarrier.name }}</strong> ({{ selectedCarrier.vessel }})</div>
                    <div>Quy mô: <strong class="text-amber-400">{{ shipment.volume }} x {{ shipment.containerType }}</strong></div>
                    <div>Tổng Giá Vốn: <strong class="text-blue-400">${{ (selectedCarrier.totalBuyCost * shipment.volume).toLocaleString() }} USD</strong></div>
                    <div>Tổng Doanh Thu: <strong class="text-emerald-400">${{ totalRevenue.toLocaleString() }} USD</strong></div>
                    <div>Tổng Lợi Nhuận Gộp: <strong :class="selectedCarrier.totalProfit >= 0 ? 'text-emerald-400' : 'text-rose-400'">${{ selectedCarrier.totalProfit.toLocaleString() }} USD</strong></div>
                </div>

                <div class="p-3 bg-amber-500/10 border border-amber-500/30 rounded-lg text-xs text-amber-300">
                    <i class="fa-solid fa-triangle-exclamation mr-1"></i> Đây là thao tác mô phỏng trên hệ thống nội bộ. Chưa phát hành booking thật sang hệ thống EDI/API hãng tàu.
                </div>

                <div class="flex justify-end gap-3 pt-2">
                    <button @click="showModal = false" class="px-4 py-2 bg-slate-700 hover:bg-slate-600 rounded-xl text-xs font-semibold transition">Đóng</button>
                    <button @click="confirmBooking" class="px-4 py-2 bg-blue-600 hover:bg-blue-500 text-white rounded-xl text-xs font-semibold transition">Xác Nhận Đặt Chỗ</button>
                </div>
            </div>
        </div>

        <!-- Modal Tách Lô (Split Batch) -->
        <div v-if="showSplitModal" class="fixed inset-0 bg-black/70 backdrop-blur-sm flex items-center justify-center p-4 z-50">
            <div class="bg-slate-800 border border-slate-700 rounded-2xl p-6 max-w-lg w-full space-y-4 shadow-2xl">
                <h3 class="text-lg font-bold text-slate-100 flex items-center gap-2">
                    <i class="fa-solid fa-scissors text-amber-400"></i> Phương Án Tách Lô (Split Shipment)
                </h3>
                
                <div v-if="selectedCarrier" class="text-xs space-y-3 text-slate-300">
                    <p>Hãng tàu <strong>{{ selectedCarrier.name }}</strong> chỉ còn đáp ứng <strong>{{ selectedCarrier.spaceAvailable }} / {{ shipment.volume }} cont</strong>. Hệ thống đề xuất phương án chia lô:</p>
                    
                    <div class="bg-slate-900 p-3 rounded-xl border border-slate-700 space-y-2">
                        <div class="flex justify-between font-semibold text-slate-200">
                            <span>Phần 1: Đi chuyến {{ selectedCarrier.name }}</span>
                            <span class="text-emerald-400">{{ selectedCarrier.spaceAvailable }} Cont</span>
                        </div>
                        <div class="flex justify-between font-semibold text-slate-200">
                            <span>Phần 2: Mua bù từ Sàn Slot dự phòng</span>
                            <span class="text-amber-400">{{ shipment.volume - selectedCarrier.spaceAvailable }} Cont</span>
                        </div>
                    </div>

                    <div class="p-3 bg-blue-500/10 border border-blue-500/30 rounded-lg text-blue-300">
                        <i class="fa-solid fa-circle-info mr-1"></i> Phương án này giúp bảo toàn tiến độ giao hàng trước hạn chót của khách, tránh rủi ro rớt toàn bộ lô 5 container.
                    </div>
                </div>

                <div class="flex justify-end gap-3 pt-2">
                    <button @click="showSplitModal = false" class="px-4 py-2 bg-slate-700 hover:bg-slate-600 rounded-xl text-xs font-semibold transition">Hủy</button>
                    <button @click="confirmSplitBatch" class="px-4 py-2 bg-amber-600 hover:bg-amber-500 text-white rounded-xl text-xs font-semibold transition">Phê Duyệt Phương Án Tách Lô</button>
                </div>
            </div>
        </div>

    </div>

    <!-- Vue.js Logic Script -->
    <script>
        const { createApp } = Vue;

        createApp({
            data() {
                return {
                    sortBy: 'profit',
                    showModal: false,
                    showSplitModal: false,
                    selectedCarrier: null,

                    // Module 3: Thông tin lô hàng (Case lịch sử QA Furniture)
                    shipment: {
                        shipper: 'QA Furniture Co., Ltd (Bình Phước)',
                        rfqId: 'RFQ-2025-0608',
                        pol: 'Cái Mép (VNVUT)',
                        pod: 'Los Angeles (USLAX)',
                        containerType: "40'HC",
                        volume: 5,
                        cargoDesc: 'Wooden kitchen cabinets (HS 940340)',
                        crd: '2025-05-28',
                        etdDesired: '2025-06-08',
                        toleranceDays: 3,
                        salesPerson: 'Bắp (Sales Forwarding)',
                        notes: 'Lô hàng cần về trước mốc rà soát thuế quan Mỹ.'
                    },

                    // Module 4.2: Quản lý giá bán
                    pricing: {
                        sellRate: 5438,
                        validUntil: '2025-06-15'
                    },

                    // Module 7 & 4.1: Danh sách các hãng tàu & giá mua chi tiết
                    carriers: [
                        {
                            id: 1,
                            name: 'Wan Hai Lines',
                            code: 'WHL',
                            vessel: 'WAN HAI A01 E012',
                            etd: '10/06/2025',
                            delayDays: 2,
                            spaceAvailable: 3, // Thiếu space cho lô 5 cont
                            oceanFreight: 4800,
                            pss: 300,
                            localCharges: 100,
                            reserveCost: 30,
                            priceValid: true,
                            isCaseDefault: true
                        },
                        {
                            id: 2,
                            name: 'Evergreen Line',
                            code: 'EMC',
                            vessel: 'EVER GIVEN / 0421E',
                            etd: '09/06/2025',
                            delayDays: 0,
                            spaceAvailable: 5,
                            oceanFreight: 4850,
                            pss: 300,
                            localCharges: 100,
                            reserveCost: 30,
                            priceValid: true,
                            isCaseDefault: false
                        },
                        {
                            id: 3,
                            name: 'COSCO Shipping',
                            code: 'COS',
                            vessel: 'COSCO VIETNAM / 015E',
                            etd: '12/06/2025',
                            delayDays: 1,
                            spaceAvailable: 5,
                            oceanFreight: 4820,
                            pss: 300,
                            localCharges: 100,
                            reserveCost: 30,
                            priceValid: false, // Giả định giá mua hết hạn cần xác minh
                            isCaseDefault: false
                        }
                    ],

                    // Module 8: Sàn slot dự phòng
                    secondarySlots: [
                        { id: 101, provider: 'VinaFreighter Logistics', carrier: 'Evergreen', availableSlots: 2, buyCost: 5240, etd: '07/06/2025' },
                        { id: 102, provider: 'Global Forwarding Partner', carrier: 'COSCO', availableSlots: 3, buyCost: 5220, etd: '09/06/2025' }
                    ]
                }
            },
            computed: {
                totalRevenue() {
                    return this.pricing.sellRate * this.shipment.volume;
                },

                // Module 5: Công thức tài chính chuẩn hóa cho từng hãng tàu
                processedCarriers() {
                    return this.carriers.map(c => {
                        const totalBuyCost = c.oceanFreight + c.pss + c.localCharges + c.reserveCost;
                        const profitPerCont = this.pricing.sellRate - totalBuyCost;
                        const totalProfit = profitPerCont * this.shipment.volume;
                        const marginPercent = this.pricing.sellRate > 0 ? ((profitPerCont / this.pricing.sellRate) * 100).toFixed(2) : 0;

                        return {
                            ...c,
                            totalBuyCost,
                            profitPerCont,
                            totalProfit,
                            marginPercent
                        };
                    });
                },

                sortedCarriers() {
                    let list = [...this.processedCarriers];
                    if (this.sortBy === 'profit') {
                        list.sort((a, b) => b.totalProfit - a.totalProfit);
                    } else if (this.sortBy === 'space') {
                        list.sort((a, b) => b.spaceAvailable - a.spaceAvailable);
                    } else if (this.sortBy === 'rate') {
                        list.sort((a, b) => a.totalBuyCost - b.totalBuyCost);
                    }
                    return list;
                },

                // Module 9: Cảnh báo nghiệp vụ tự động
                operationalWarnings() {
                    let warnings = [];
                    if (this.shipment.volume <= 0) {
                        warnings.push({ type: 'danger', title: 'Lỗi Số Lượng Cont', desc: 'Số lượng container phải lớn hơn 0.' });
                    }
                    // Kiểm tra giá mua hết hạn
                    const expiredCount = this.carriers.filter(c => !c.priceValid).length;
                    if (expiredCount > 0) {
                        warnings.push({ type: 'amber', title: 'Giá Mua Hết Hạn', desc: `Có ${expiredCount} hãng tàu có báo giá mua đã hết hạn hiệu lực, cần cập nhật lại từ line.` });
                    }
                    // Kiểm tra thiếu space
                    const maxSpace = Math.max(...this.carriers.map(c => c.spaceAvailable));
                    if (maxSpace < this.shipment.volume) {
                        warnings.push({ type: 'danger', title: 'Thiếu Space Trầm Trọng', desc: `Yêu cầu ${this.shipment.volume} cont nhưng không có hãng tàu đơn lẻ nào đáp ứng đủ. Cần dùng phương án Tách Lô.` });
                    }
                    // Kiểm tra biên lợi nhuận thấp
                    const lowMargin = this.processedCarriers.filter(c => c.marginPercent < 5);
                    if (lowMargin.length > 0) {
                        warnings.push({ type: 'amber', title: 'Biên Lợi Nhuận Thấp', desc: 'Một số phương án có biên lợi nhuận gộp dưới 5%, rất nhạy cảm với chi phí phát sinh.' });
                    }
                    return warnings;
                }
            },
            methods: {
                loadHistoricalCase() {
                    this.shipment = {
                        shipper: 'QA Furniture Co., Ltd (Bình Phước)',
                        rfqId: 'RFQ-2025-0608',
                        pol: 'Cái Mép (VNVUT)',
                        pod: 'Los Angeles (USLAX)',
                        containerType: "40'HC",
                        volume: 5,
                        cargoDesc: 'Wooden kitchen cabinets (HS 940340)',
                        crd: '2025-05-28',
                        etdDesired: '2025-06-08',
                        toleranceDays: 3,
                        salesPerson: 'Bắp (Sales Forwarding)',
                        notes: 'Case lịch sử: Lô hàng 5 cont xuất Mỹ bằng tàu Wan Hai, trễ ETD 2 ngày.'
                    };
                    this.pricing.sellRate = 5438;
                    alert('Đã khôi phục thành công bộ dữ liệu Case lịch sử QA Furniture!');
                },
                exportDataJSON() {
                    const dataStr = "data:text/json;charset=utf-8," + encodeURIComponent(JSON.stringify({ shipment: this.shipment, pricing: this.pricing, carriers: this.processedCarriers }, null, 2));
                    const downloadAnchor = document.createElement('a');
                    downloadAnchor.setAttribute("href", dataStr);
                    downloadAnchor.setAttribute("download", `LogiSpace_Report_${this.shipment.rfqId}.json`);
                    document.body.appendChild(downloadAnchor);
                    downloadAnchor.click();
                    downloadAnchor.remove();
                },
                openBookingModal(carrier) {
                    this.selectedCarrier = carrier;
                    this.showModal = true;
                },
                confirmBooking() {
                    alert(`Đã ghi nhận đặt chỗ mô phỏng thành công trên hãng ${this.selectedCarrier.name}!`);
                    this.showModal = false;
                },
                openSplitModal(carrier) {
                    this.selectedCarrier = carrier;
                    this.showSplitModal = true;
                },
                confirmSplitBatch() {
                    alert(`Đã phê duyệt phương án tách lô: ${this.selectedCarrier.spaceAvailable} cont đi chuyến ${this.selectedCarrier.name} và phần còn lại mua bù từ sàn slot dự phòng.`);
                    this.showSplitModal = false;
                },
                claimSecondarySlot(slot) {
                    alert(`Đã nhận nhượng thành công ${slot.availableSlots} slot từ ${slot.provider}!`);
                }
            }
        }).mount('#app');
    </script>
</body>
</html>
