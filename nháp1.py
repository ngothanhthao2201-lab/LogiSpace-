import streamlit as st

st.set_page_config(
    page_title="LogiSpace Simulator — Freight Quotation & Space Intelligence Platform",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# === CSS TÙY CHỈNH FULL MÀN HÌNH VÀ ẨN MENU STREAMLIT ===
st.markdown("""
    <style>
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}
        
        .block-container {
            padding-top: 0rem !important;
            padding-bottom: 0rem !important;
            padding-left: 0rem !important;
            padding-right: 0rem !important;
            max-width: 100% !important;
        }
        
        .stApp {
            margin: 0px;
            background-color: #0f172a;
        }
    </style>
""", unsafe_allow_html=True)

html_code = """
<!DOCTYPE html>
<html lang="vi">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>LogiSpace Simulator</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
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
        
        <!-- HEADER -->
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
                 
                 <div class="flex flex-wrap items-center gap-1 bg-slate-900 p-1 rounded-xl border border-slate-800">
                    <button @click="currentTab = 'dashboard'" :class="currentTab === 'dashboard' ? 'bg-blue-600 text-white shadow' : 'text-slate-400 hover:text-slate-200'" class="px-3 py-1.5 rounded-lg text-xs font-medium transition">
                          <i class="fa-solid fa-chart-pie mr-1"></i> Dashboard
                    </button>
                    <button @click="currentTab = 'shipmentForm'" :class="currentTab === 'shipmentForm' ? 'bg-blue-600 text-white shadow' : 'text-slate-400 hover:text-slate-200'" class="px-3 py-1.5 rounded-lg text-xs font-medium transition">
                          <i class="fa-solid fa-pen-to-square mr-1"></i> Thông Tin Lô Hàng
                    </button>
                    <button @click="currentTab = 'quotation'" :class="currentTab === 'quotation' ? 'bg-blue-600 text-white shadow' : 'text-slate-400 hover:text-slate-200'" class="px-3 py-1.5 rounded-lg text-xs font-medium transition">
                          <i class="fa-solid fa-calculator mr-1"></i> Báo Giá & Biên Lãi
                    </button>
                    <button @click="currentTab = 'spaceForecast'" :class="currentTab === 'spaceForecast' ? 'bg-blue-600 text-white shadow' : 'text-slate-400 hover:text-slate-200'" class="px-3 py-1.5 rounded-lg text-xs font-medium transition">
                          <i class="fa-solid fa-shield-halved mr-1"></i> Dự Báo Space
                    </button>
                    <button @click="currentTab = 'peakSeason'" :class="currentTab === 'peakSeason' ? 'bg-blue-600 text-white shadow' : 'text-slate-400 hover:text-slate-200'" class="px-3 py-1.5 rounded-lg text-xs font-medium transition">
                          <i class="fa-solid fa-triangle-exclamation mr-1"></i> Mùa Cao Điểm Thuế
                    </button>
                    <button @click="currentTab = 'marketplace'" :class="currentTab === 'marketplace' ? 'bg-blue-600 text-white shadow' : 'text-slate-400 hover:text-slate-200'" class="px-3 py-1.5 rounded-lg text-xs font-medium transition">
                          <i class="fa-solid fa-right-left mr-1"></i> Sàn Slot Marketplace
                    </button>
                 </div>
            </div>
        </header>

        <main class="flex-1 w-full p-4 md:p-6 space-y-6">
            <div class="bg-slate-800/80 border border-slate-700 rounded-2xl p-4 flex flex-col md:flex-row items-center justify-between gap-3 text-xs shadow-lg w-full">
                 <div class="flex items-center gap-3">
                     <span class="w-2.5 h-2.5 rounded-full bg-emerald-400 animate-pulse"></span>
                     <div>
                         <strong class="text-white">Trạng thái đồng bộ:</strong>
                         <span class="px-2 py-0.5 rounded bg-emerald-500/20 text-emerald-300 border border-emerald-500/30 font-medium">Đã nạp dữ liệu chuẩn (QA Furniture - Cái Mép / LAX)</span>
                         (Cập nhật lúc: <span class="text-slate-300 font-mono">{{ lastUpdatedTime }}</span>).
                     </div>
                 </div>
                 <div class="flex items-center gap-3">
                     <button @click="resetToDefault" class="bg-slate-700 hover:bg-slate-600 text-slate-200 px-3 py-1 rounded-lg transition font-medium">
                         Đặt Lại Dữ Liệu Chuẩn
                     </button>
                 </div>
            </div>

            <!-- TAB 1: DASHBOARD -->
            <div v-if="currentTab === 'dashboard'" class="space-y-6 w-full">
                 <div class="grid grid-cols-1 md:grid-cols-4 gap-4 w-full">
                     <div class="bg-slate-800/60 border border-slate-700/60 rounded-2xl p-5 shadow-lg">
                         <div class="text-xs text-slate-400 mb-1">Quy Mô Lô Hàng</div>
                         <div class="text-2xl font-bold text-white">{{ shipment.volume }} x {{ shipment.containerType }}</div>
                         <div class="text-[11px] text-blue-400 mt-2">Tuyến: {{ shipment.pol }} → {{ shipment.pod }}</div>
                     </div>
                     <div class="bg-slate-800/60 border border-slate-700/60 rounded-2xl p-5 shadow-lg">
                         <div class="text-xs text-slate-400 mb-1">Biên Lợi Nhuận Gộp Thực Tế</div>
                         <div class="text-2xl font-bold text-amber-400">{{ calculatedMargin }}%</div>
                         <div class="text-[11px] text-slate-400 mt-2">Mục tiêu chuẩn: {{ targetMargin }}% (Nhạy cảm chi phí)</div>
                     </div>
                     <div class="bg-slate-800/60 border border-slate-700/60 rounded-2xl p-5 shadow-lg">
                         <div class="text-xs text-slate-400 mb-1">Rủi Ro Trễ Tàu (Rolling Risk)</div>
                         <div class="text-2xl font-bold text-rose-400">+{{ shipment.rollingDays }} Ngày Chậm</div>
                         <div class="text-[11px] text-slate-400 mt-2">ETD kế hoạch: {{ shipment.etd }}</div>
                     </div>
                     <div class="bg-slate-800/60 border border-slate-700/60 rounded-2xl p-5 shadow-lg">
                         <div class="text-xs text-slate-400 mb-1">Slot Sẵn Sàng Trên Sàn</div>
                         <div class="text-2xl font-bold text-emerald-400">{{ filteredMarketplaceList.length }} Tin Đăng</div>
                         <div class="text-[11px] text-slate-400 mt-2">Giải pháp bù đắp thiếu hụt space</div>
                     </div>
                 </div>

                 <div class="grid grid-cols-1 lg:grid-cols-2 gap-6 w-full">
                     <div class="bg-slate-800/80 border border-slate-700/80 rounded-2xl p-5 shadow-xl space-y-4">
                         <h3 class="text-sm font-bold text-slate-200 flex items-center gap-2">
                             <i class="fa-solid fa-bolt text-amber-400"></i> Hồ Sơ Lô Hàng Đang Khảo Sát
                         </h3>
                         <div class="space-y-2 text-xs text-slate-300">
                             <div><strong>Shipper / Consignee:</strong> {{ shipment.shipper }} / {{ shipment.consignee }}</div>
                             <div><strong>Mặt hàng:</strong> {{ shipment.commodity }}</div>
                             <div><strong>Booking / MBL:</strong> 039FX49604 | <strong>Vessel:</strong> WAN HAI A01 E012</div>
                             <div><strong>Ngày Book (Booking Date):</strong> <span class="text-amber-300 font-bold">2025</span>-05-12</div>
                             <div class="p-3 mt-2 rounded-xl bg-rose-500/10 border border-rose-500/30 text-rose-300">
                                 <i class="fa-solid fa-triangle-exclamation mr-1"></i> 
                                 Cảnh báo: Yêu cầu giữ chỗ đồng thời số lượng lớn đối mặt rủi ro thiếu space trầm trọng do làn sóng đẩy hàng trước chính sách thuế quan.
                             </div>
                         </div>
                     </div>

                     <div class="bg-slate-800/80 border border-slate-700/80 rounded-2xl p-5 shadow-xl space-y-4">
                         <h3 class="text-sm font-bold text-slate-200 flex items-center gap-2">
                             <i class="fa-solid fa-circle-info text-blue-400"></i> Hướng Dẫn Sử Dụng Nút Cập Nhật
                         </h3>
                         <p class="text-xs text-slate-300 leading-relaxed">
                             Truy cập tab <strong>Thông Tin Lô Hàng</strong> để thay đổi cảng, loại container hoặc số lượng. Sau đó nhấn nút <strong>“Hoàn thành và cập nhật dữ liệu”</strong> để toàn bộ hệ thống tính toán lại giá mua, giá bán, biên lãi và rủi ro theo đúng quy trình kiểm thử nghiệp vụ Sales Forwarding.
                         </p>
                     </div>
                 </div>
            </div>

            <!-- TAB 2: THÔNG TIN LÔ HÀNG -->
            <div v-if="currentTab === 'shipmentForm'" class="space-y-6 w-full">
                <div class="bg-slate-800/80 border border-slate-700/80 rounded-2xl p-6 shadow-xl space-y-5">
                    <h3 class="text-sm font-bold text-slate-200 flex items-center gap-2">
                        <i class="fa-solid fa-pen-to-square text-blue-400"></i> Cập Nhật Tham Số Lô Hàng Thực Tế
                    </h3>
                    
                    <div class="grid grid-cols-1 md:grid-cols-3 gap-4 text-xs">
                        <div>
                            <label class="block text-slate-400 mb-1 font-medium">Shipper</label>
                            <input type="text" v-model="shipment.shipper" class="w-full bg-slate-900 border border-slate-700 rounded-lg px-3 py-2 text-slate-200 focus:outline-none focus:border-blue-500">
                        </div>
                        <div>
                            <label class="block text-slate-400 mb-1 font-medium">Consignee</label>
                            <input type="text" v-model="shipment.consignee" class="w-full bg-slate-900 border border-slate-700 rounded-lg px-3 py-2 text-slate-200 focus:outline-none focus:border-blue-500">
                        </div>
                        <div>
                            <label class="block text-slate-400 mb-1 font-medium">Mặt Hàng (Commodity)</label>
                            <input type="text" v-model="shipment.commodity" class="w-full bg-slate-900 border border-slate-700 rounded-lg px-3 py-2 text-slate-200 focus:outline-none focus:border-blue-500">
                        </div>
                        <div>
                            <label class="block text-slate-400 mb-1 font-medium">Cảng Đi (POL)</label>
                            <select v-model="shipment.pol" class="w-full bg-slate-900 border border-slate-700 rounded-lg px-3 py-2 text-slate-200 focus:outline-none focus:border-blue-500">
                                <option value="VNTAN (Cái Mép)">VNTAN (Cái Mép)</option>
                                <option value="VNHPH (Hải Phòng)">VNHPH (Hải Phòng)</option>
                                <option value="VNSGN (Cat Lai)">VNSGN (Cat Lai)</option>
                            </select>
                        </div>
                        <div>
                            <label class="block text-slate-400 mb-1 font-medium">Cảng Đến (POD)</label>
                            <select v-model="shipment.pod" class="w-full bg-slate-900 border border-slate-700 rounded-lg px-3 py-2 text-slate-200 focus:outline-none focus:border-blue-500">
                                <option value="USLAX (Los Angeles)">USLAX (Los Angeles)</option>
                                <option value="USLGB (Long Beach)">USLGB (Long Beach)</option>
                                <option value="USOAK (Oakland)">USOAK (Oakland)</option>
                            </select>
                        </div>
                        <div>
                            <label class="block text-slate-400 mb-1 font-medium">Loại Container</label>
                            <select v-model="shipment.containerType" class="w-full bg-slate-900 border border-slate-700 rounded-lg px-3 py-2 text-slate-200 focus:outline-none focus:border-blue-500">
                                <option value="40'HC">40'HC</option>
                                <option value="20'DC">20'DC</option>
                                <option value="45'HC">45'HC</option>
                            </select>
                        </div>
                        <div>
                            <label class="block text-slate-400 mb-1 font-medium">Số Lượng (Volume)</label>
                            <input type="number" v-model.number="shipment.volume" class="w-full bg-slate-900 border border-slate-700 rounded-lg px-3 py-2 text-slate-200 focus:outline-none focus:border-blue-500">
                        </div>
                        <div>
                            <label class="block text-slate-400 mb-1 font-medium">Ngày Book (Booking Date - <span class="text-amber-300">2025</span>)</label>
                            <input type="date" v-model="shipment.bookingDate" class="w-full bg-slate-900 border border-slate-700 rounded-lg px-3 py-2 text-slate-200 focus:outline-none focus:border-blue-500">
                        </div>
                        <div>
                            <label class="block text-slate-400 mb-1 font-medium">ETD Dự Kiến</label>
                            <input type="date" v-model="shipment.etd" class="w-full bg-slate-900 border border-slate-700 rounded-lg px-3 py-2 text-slate-200 focus:outline-none focus:border-blue-500">
                        </div>
                    </div>

                    <div class="flex justify-end pt-4">
                        <button @click="updateShipmentData" class="bg-blue-600 hover:bg-blue-500 text-white font-medium px-5 py-2.5 rounded-xl transition text-xs shadow-lg shadow-blue-600/30">
                            <i class="fa-solid fa-check mr-1.5"></i> Hoàn thành và cập nhật dữ liệu
                        </button>
                    </div>
                </div>
            </div>

            <!-- TAB 3: BÁO GIÁ & BIÊN LÃI -->
            <div v-if="currentTab === 'quotation'" class="space-y-6 w-full">
                <div class="bg-slate-800/80 border border-slate-700/80 rounded-2xl p-6 shadow-xl space-y-4">
                    <h3 class="text-sm font-bold text-slate-200 flex items-center gap-2">
                        <i class="fa-solid fa-calculator text-emerald-400"></i> Bảng Phân Tích Cấu Trúc Giá & Lợi Nhuận Gộp
                    </h3>
                    <div class="overflow-x-auto">
                        <table class="w-full text-left text-xs text-slate-300 border-collapse">
                            <thead>
                                <tr class="border-b border-slate-700 text-slate-400">
                                    <th class="py-3 px-4">Khoản Mục Chi Phí / Doanh Thu</th>
                                    <th class="py-3 px-4 text-right">Giá Mua (Buying Rate)</th>
                                    <th class="py-3 px-4 text-right">Giá Bán (Selling Rate)</th>
                                    <th class="py-3 px-4 text-right">Lợi Nhuận (Gross Profit)</th>
                                </tr>
                            </thead>
                            <tbody class="divide-y divide-slate-700/60">
                                <tr>
                                    <td class="py-3 px-4 font-medium text-white">Ocean Freight (Cước biển chính)</td>
                                    <td class="py-3 px-4 text-right">${{ quotation.buyingFreight }}</td>
                                    <td class="py-3 px-4 text-right">${{ quotation.sellingFreight }}</td>
                                    <td class="py-3 px-4 text-right text-emerald-400 font-semibold">${{ quotation.sellingFreight - quotation.buyingFreight }}</td>
                                </tr>
                                <tr>
                                    <td class="py-3 px-4 font-medium text-white">Local Charges (Phụ phí địa phương tại POL)</td>
                                    <td class="py-3 px-4 text-right">${{ quotation.buyingLocalPOL }}</td>
                                    <td class="py-3 px-4 text-right">${{ quotation.sellingLocalPOL }}</td>
                                    <td class="py-3 px-4 text-right text-emerald-400 font-semibold">${{ quotation.sellingLocalPOL - quotation.buyingLocalPOL }}</td>
                                </tr>
                                <tr>
                                    <td class="py-3 px-4 font-medium text-white">Destination Surcharges (Phụ phí đến POD)</td>
                                    <td class="py-3 px-4 text-right">${{ quotation.buyingLocalPOD }}</td>
                                    <td class="py-3 px-4 text-right">${{ quotation.sellingLocalPOD }}</td>
                                    <td class="py-3 px-4 text-right text-emerald-400 font-semibold">${{ quotation.sellingLocalPOD - quotation.buyingLocalPOD }}</td>
                                </tr>
                                <tr class="bg-slate-900/60 font-bold text-white">
                                    <td class="py-3 px-4">TỔNG CỘNG (CHO {{ shipment.volume }} CONTAINER)</td>
                                    <td class="py-3 px-4 text-right">${{ totalBuying }}</td>
                                    <td class="py-3 px-4 text-right">${{ totalSelling }}</td>
                                    <td class="py-3 px-4 text-right text-amber-400">${{ totalProfit }} ({{ calculatedMargin }}%)</td>
                                </tr>
                            </tbody>
                        </table>
                    </div>
                </div>
            </div>

            <!-- TAB 4: DỰ BÁO SPACE -->
            <div v-if="currentTab === 'spaceForecast'" class="space-y-6 w-full">
                <div class="bg-slate-800/80 border border-slate-700/80 rounded-2xl p-6 shadow-xl space-y-4">
                    <h3 class="text-sm font-bold text-slate-200 flex items-center gap-2">
                        <i class="fa-solid fa-shield-halved text-blue-400"></i> Mô Hình Dự Báo Rủi Ro Thiếu Hụt Chỗ (Space Shortage)
                    </h3>
                    <div class="grid grid-cols-1 md:grid-cols-3 gap-4 text-xs">
                        <div class="bg-slate-900/60 border border-slate-700 p-4 rounded-xl space-y-2">
                            <div class="text-slate-400">Tỷ Lệ Đầy Tàu (Vessel Utilization)</div>
                            <div class="text-xl font-bold text-rose-400">96.5%</div>
                            <p class="text-slate-400 text-[11px]">Tàu đã gần như cạn sạch chỗ trống trên tuyến Cái Mép - LAX.</p>
                        </div>
                        <div class="bg-slate-900/60 border border-slate-700 p-4 rounded-xl space-y-2">
                            <div class="text-slate-400">Khả Năng Bị Rớt Tàu (Rolling Probability)</div>
                            <div class="text-xl font-bold text-amber-400">High (78%)</div>
                            <p class="text-slate-400 text-[11px]">Rủi ro cao nếu không chốt bảo đảm space hoặc mua bổ sung slot.</p>
                        </div>
                        <div class="bg-slate-900/60 border border-slate-700 p-4 rounded-xl space-y-2">
                            <div class="text-slate-400">Khuyến Nghị Hành Động</div>
                            <div class="text-xl font-bold text-emerald-400">Mua Sàn Slot</div>
                            <p class="text-slate-400 text-[11px]">Sử dụng Sàn Slot Marketplace để cover phần thiếu hụt ngay lập tức.</p>
                        </div>
                    </div>
                </div>
            </div>

            <!-- TAB 5: MÙA CAO ĐIỂM THUẾ -->
            <div v-if="currentTab === 'peakSeason'" class="space-y-6 w-full">
                <div class="bg-slate-800/80 border border-slate-700/80 rounded-2xl p-6 shadow-xl space-y-4">
                    <h3 class="text-sm font-bold text-slate-200 flex items-center gap-2">
                        <i class="fa-solid fa-triangle-exclamation text-amber-400"></i> Phân Tích Làn Sóng Hàng Hóa Trước Chính Sách Thuế Quan
                    </h3>
                    <p class="text-xs text-slate-300 leading-relaxed">
                        Thị trường đang chứng kiến đợt đẩy hàng (front-loading) ồ ạt từ các chủ hàng nội thất và hàng tiêu dùng nhằm né tránh các khung thuế chống bán phá giá và biểu thuế mới sắp được công bố. Điều này tạo áp lực cực lớn lên booking slot tại khu vực Cái Mép và Cát Lái, đẩy giá cước giao ngay (Spot rate) tăng phi mã.
                    </p>
                </div>
            </div>

            <!-- TAB 6: SÀN SLOT MARKETPLACE -->
            <div v-if="currentTab === 'marketplace'" class="space-y-6 w-full">
                <div class="bg-slate-800/80 border border-slate-700/80 rounded-2xl p-6 shadow-xl space-y-4">
                    <h3 class="text-sm font-bold text-slate-200 flex items-center gap-2">
                        <i class="fa-solid fa-right-left text-blue-400"></i> Sàn Giao Dịch Slot & Chia Sẻ Space Chủ Hàng
                    </h3>
                    <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
                        <div v-for="(item, index) in marketplaceList" :key="index" class="bg-slate-900/60 border border-slate-700 p-4 rounded-xl space-y-3 text-xs">
                            <div class="flex justify-between items-center">
                                <span class="font-bold text-white">{{ item.route }}</span>
                                <span class="px-2 py-0.5 rounded bg-blue-500/20 text-blue-300 font-medium">{{ item.slots }} Slot sẵn</span>
                            </div>
                            <div class="text-slate-300">Carrier: <span class="text-white font-medium">{{ item.carrier }}</span> | ETD: {{ item.etd }}</div>
                            <div class="flex justify-between items-center pt-2 border-t border-slate-800">
                                <span class="text-amber-400 font-bold">${{ item.price }}/container</span>
                                <button @click="bookMarketplaceSlot(index)" class="bg-emerald-600 hover:bg-emerald-500 text-white px-3 py-1.5 rounded-lg transition font-medium">
                                    Đăng Ký Mua Slot
                                </button>
                            </div>
                        </div>
                    </div>
                </div>
            </div>

        </main>
    </div>

    <script>
        const { createApp, ref, computed } = Vue;

        createApp({
            setup() {
                const currentTab = ref('dashboard');
                const lastUpdatedTime = ref(new Date().toLocaleTimeString());
                const targetMargin = ref(15);

                const shipment = ref({
                    shipper: 'QA Furniture Co., Ltd',
                    consignee: 'American Home Furnishings Inc.',
                    commodity: 'Wooden Dining Tables & Chairs',
                    pol: 'VNTAN (Cái Mép)',
                    pod: 'USLAX (Los Angeles)',
                    containerType: "40'HC",
                    volume: 12,
                    bookingDate: '2025-05-12',
                    etd: '2025-06-01',
                    rollingDays: 2
                });

                const quotation = ref({
                    buyingFreight: 3200,
                    sellingFreight: 3450,
                    buyingLocalPOL: 150,
                    sellingLocalPOL: 220,
                    buyingLocalPOD: 400,
                    sellingLocalPOD: 480
                });

                const marketplaceList = ref([
                    { route: 'Cái Mép → Los Angeles', carrier: 'WAN HAI', slots: 5, etd: '2025-06-05', price: 3350 },
                    { route: 'Cái Mép → Long Beach', carrier: 'COSCO', slots: 3, etd: '2025-06-08', price: 3400 },
                    { route: 'Hải Phòng → Oakland', carrier: 'EVERGREEN', slots: 2, etd: '2025-06-10', price: 3250 }
                ]);

                const filteredMarketplaceList = computed(() => marketplaceList.value);

                const totalBuying = computed(() => {
                    return (quotation.value.buyingFreight + quotation.value.buyingLocalPOL + quotation.value.buyingLocalPOD) * shipment.value.volume;
                });

                const totalSelling = computed(() => {
                    return (quotation.value.sellingFreight + quotation.value.sellingLocalPOL + quotation.value.sellingLocalPOD) * shipment.value.volume;
                });

                const totalProfit = computed(() => {
                    return totalSelling.value - totalBuying.value;
                });

                const calculatedMargin = computed(() => {
                    if (totalSelling.value === 0) return 0;
                    return ((totalProfit.value / totalSelling.value) * 100).toFixed(1);
                });

                const updateShipmentData = () => {
                    lastUpdatedTime.value = new Date().toLocaleTimeString();
                    currentTab.value = 'dashboard';
                    alert('Đã cập nhật thành công thông tin lô hàng và làm mới bảng tính!');
                };

                const resetToDefault = () => {
                    shipment.value = {
                        shipper: 'QA Furniture Co., Ltd',
                        consignee: 'American Home Furnishings Inc.',
                        commodity: 'Wooden Dining Tables & Chairs',
                        pol: 'VNTAN (Cái Mép)',
                        pod: 'USLAX (Los Angeles)',
                        containerType: "40'HC",
                        volume: 12,
                        bookingDate: '2025-05-12',
                        etd: '2025-06-01',
                        rollingDays: 2
                    };
                    lastUpdatedTime.value = new Date().toLocaleTimeString();
                    alert('Đã khôi phục dữ liệu chuẩn!');
                };

                const bookMarketplaceSlot = (idx) => {
                    alert('Đăng ký mua thành công ' + marketplaceList.value[idx].route + '!');
                };

                return {
                    currentTab,
                    lastUpdatedTime,
                    targetMargin,
                    shipment,
                    quotation,
                    marketplaceList,
                    filteredMarketplaceList,
                    totalBuying,
                    totalSelling,
                    totalProfit,
                    calculatedMargin,
                    updateShipmentData,
                    resetToDefault,
                    bookMarketplaceSlot
                };
            }
        }).mount('#app');
    </script>
</body>
</html>
"""

st.components.v1.html(html_code, height=900, scrolling=True)
