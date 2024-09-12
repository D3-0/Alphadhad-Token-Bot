from aiogram.utils.markdown import hide_link

# Add other languages and their corresponding codes as needed.
SUPPORTED_LANGUAGES = {
    "ru": "🇸🇦 العربية",
    "en": "🇬🇧 English",
}

TEXT_BUTTONS = {
    "ru": {
        "add": "➕ إضافة",
        "back": "↩ العودة",
        "main": "🏠 الرئيسية",
        "retry": "🔄 إعادة المحاولة",
        "delete": "❌ حذف",
        "confirm": "✅ تأكيد",

        "connect_wallet": "ربط {wallet_name}",
        "open_wallet": "انتقل إلى {wallet_name}",
        "disconnect_wallet": "❌ فصل المحفظة",

        "change_language": "🔄 تغيير اللغة",
        "get_access": "🔍 التحقق من الوصول",

        "newsletter": "📰 النشرة الإخبارية",
        "admins_menu": "👥 المشرفين",
        "chats_menu": "💬 المحادثات",
        "tokens_menu": "💎 الرموز المميزة",
        "edit_min_amount": "✎ تعديل الحد الأدنى للمبلغ",
    },
    "en": {
        "add": "➕ Add",
        "back": "↩ Back",
        "main": "🏠 Main",
        "retry": "🔄 Retry",
        "delete": "❌ Delete",
        "confirm": "✅ Confirm",

        "connect_wallet": "Connect {wallet_name}",
        "open_wallet": "Go to {wallet_name}",
        "disconnect_wallet": "❌ Disconnect",

        "change_language": "🔄 Change Language",
        "get_access": "🔍 Check access availability",

        "newsletter": "📰 Newsletter",
        "admins_menu": "👥 Admins",
        "chats_menu": "💬 Chats",
        "tokens_menu": "💎 Tokens",
        "edit_min_amount": "✎ Edit minimum amount",
    }
}

TEXT_MESSAGES = {
    "ru": {
        "loader_text": "⏳",
        "outdated_text": "...",

        "main_menu": (
            f"{hide_link('https://i.ibb.co/YZCzjJ4/ar1.png')}"
            "🤖 <b>مرحبا بك!</b>\n\n"
            "للحصول على صلاحية الدخول الى قنوات و خدمات الفاضاد+ ، يجب ان تمتلك محفظتك على:\n\n"
            "<blockquote><b>القنوات الخاصة:</b>\n{chats}\n"
            "<b>العملة والكمية المطلوبة:</b>\n{tokens}</blockquote>\n\n"
            "💡 ملاحظة: يمكنك شراء عملة ADHD من المنصة اللامركزية عن طريق الضغط على رمز العملة في الاعلى\n\n"
            "في حال كانت محفظتك تحتوي على هذه الكمية ، يرجى النقر على زر التحقق من الوصول في الأدنى.\n\n"
            "<b>متصل بـ:</b> {wallet}"
        ),
        "select_language": (
            f"{hide_link('https://i.ibb.co/jZNvkwn/ar2.png')}"
            "👋 <b>مرحبًا!</b>\n\n"
            "اختر اللغة:"
        ),
        "change_language": (
            f"{hide_link('https://i.ibb.co/yyTvvSW/ar3.png')}"
            "<b>اختر اللغة:</b>"
        ),
        "deny_access": (
            f"{hide_link('https://i.ibb.co/MhQfm1t/ar4.png')}"
            "🚫 <b>الوصول مرفوض</b>\n\n"
            "نأسف. لا يمكنك الوصول الى الفاضاد+ , لعدم وجود كمية العملة المطلوبة في محفظتك\n\n"
            "يمكنك إمتلاك العملة من خلال الضغط على اسم ورمز العملة أدناه,  و شرائها من المنصة اللامركزية ومن ثم إعادة المحاولة مجدداً"
        ),
        "allow_access": (
            f"{hide_link('https://i.ibb.co/s2kcBjM/ar5.png')}"
            "<b>​تهانينا ومرحبا بك! 🎉🥳 </b>\n\n"
            "تم منحك الوصول إلى الفاضاد+\n\n"
            "انقر على اسم القناة في الاسفل للإنضمام !\n\n"
            "⚠️  تنبيه: اذا قمت ببيع او تحريك الكمية المطلوبة من عملة ADHD الى محفظة اخرى ، سوف تفقد امكانية الوصول الى الفاضاد+"
        ),
        "user_kicked": (
            "تم طرد المستخدم {user} [{wallet}] من القناة الخاصة!"
        ),

        "connect_wallet": (
            f"<a href='https://ton.org/wallets?locale=en&filters[wallet_features][slug][$in]=dapp-auth&pagination[limit]=-1'>تثبيت محفظة جديدة</a>\n\n"
            "للانضمام الى <b>الفاضاد+</b>، يرجى ربط محفظتك {wallet_name} التي يوجد بها الكمية المطلوبة من عملة <b>ADHD</b>\n\n"
            "يمكنك اختيار اي من المحافظ التي في الاسفل ، قم بعمل مسح للكود الظاهر في الصورة من خلال تطبيق المحفظة على الجوال:"
        ),
        "connect_wallet_proof_wrong": (
            f"{hide_link('https://i.ibb.co/qj4R1sT/ar6.png')}"
            "<b>⚠️ تنبيه</b>\n\n"
            "توقيع المحفظة مزيف أو انتهت صلاحية وقت الانتظار للربط."
        ),
        "connect_wallet_timeout": (
            f"{hide_link('https://i.ibb.co/NxkYKb1/ar7.png')}"
            "<b>⚠️ تنبيه</b>\n\n"
            "انتهى وقت الانتظار لربط محفظتك\n\n"
            "اضغط على اعادة المحاولة.🔁"
        ),

        "admin_menu": (
            f"{hide_link('https://i.ibb.co/9HkX1y7/main.png')}"
            "<b>لوحة الإدارة</b>\n\nاختر الإجراء:"
        ),
        "chats_menu": (
            f"{hide_link('https://i.ibb.co/9HkX1y7/main.png')}"
            "<b>قائمة المحادثات الخاصة</b>\n\nاختر الإجراء:"
        ),
        "chat_info": (
            f"{hide_link('https://i.ibb.co/9HkX1y7/main.png')}"
            "• <b>معلومات عن المحادثة الخاصة</b>\n\n"
            "• <b>الرقم التعريفي:</b>\n"
            "<blockquote>{chat_id}</blockquote>\n"
            "• <b>النوع:</b>\n"
            "<blockquote>{chat_type}</blockquote>\n"
            "• <b>الاسم:</b>\n"
            "<blockquote>{chat_name}</blockquote>\n"
            "• <b>رابط الدعوة:</b>\n"
            "<blockquote>{chat_invite_link}</blockquote>\n"
            "• <b>تاريخ الإنشاء:</b>\n"
            "<blockquote>{chat_created_at}</blockquote>"
        ),
        "tokens_menu": (
            f"{hide_link('https://i.ibb.co/9HkX1y7/main.png')}"
            "<b>قائمة الرموز المميزة</b>\n\nاختر الإجراء:"
        ),
        "token_info": (
            f"{hide_link('https://i.ibb.co/9HkX1y7/main.png')}"
            "• <b>معلومات عن الرمز المميز</b>\n\n"
            "• <b>النوع:</b>\n"
            "<blockquote>{token_type}</blockquote>\n"
            "• <b>الاسم:</b>\n"
            "<blockquote>{token_name}</blockquote>\n"
            "• <b>العنوان:</b>\n"
            "<blockquote>{token_address}</blockquote>\n"
            "• <b>الحد الأدنى للمبلغ:</b>\n"
            "<blockquote>{token_min_amount}</blockquote>\n"
            "• <b>تاريخ الإنشاء:</b>\n"
            "<blockquote>{token_created_at}</blockquote>"
        ),
        "token_send_address": "<b>أدخل عنوان الرمز المميز</b>\n\nيسمح فقط بعناوين مجموعات NFT والمستشارين Jetton:",
        "token_send_address_error": "عنوان الرمز المميز غير صالح:\n{}",
        "token_send_address_error_already_exist": "الرمز المميز بالعنوان {address} موجود بالفعل!",
        "token_send_address_error_not_supported": "العقد {interfaces} غير مدعوم.\nمدعوم فقط {supported_interfaces}.",
        "token_send_amount": (
            "<b>معلومات عن الرمز المميز</b>:\n\n"
            "• <b>النوع:</b>\n{token_type}\n"
            "• <b>الاسم:</b>\n{token_name}\n\n"
            "<b>أدخل الحد الأدنى لمبلغ الرمز المميز</b> للوصول إلى المحادثة الخاصة:"
        ),
        "token_edit_amount": "<b>أدخل المبلغ الجديد للرمز المميز</b> للوصول إلى المحادثة الخاصة:",
        "token_send_amount_error": "مبلغ الرمز المميز غير صحيح!",
        "admins_menu": (
            f"{hide_link('https://i.ibb.co/9HkX1y7/main.png')}"
            "<b>قائمة المشرفين</b>\n\nاختر الإجراء:"
        ),
        "admin_info": (
            f"{hide_link('https://i.ibb.co/9HkX1y7/main.png')}"
            "• <b>معلومات عن المشرف</b>\n\n"
            "• <b>الرقم التعريفي:</b>\n"
            "<blockquote>{admin_id}</blockquote>\n"
            "• <b>الاسم:</b>\n"
            "<blockquote>{admin_full_name}</blockquote>\n"
            "• <b>اسم المستخدم:</b>\n"
            "<blockquote>{admin_username}</blockquote>\n"
            "• <b>تاريخ الإنشاء:</b>\n"
            "<blockquote>{admin_created_at}</blockquote>"
        ),
        "admin_send_id": "<b>أدخل رقم تعريف المشرف:</b>",
        "admin_send_id_error": "رقم التعريف غير صالح:\n{}",
        "admin_send_id_error_not_found": "لم يتم العثور على المشرف. يجب أن يبدأ المستخدم الدردشة مع البوت أولاً.",
        "admin_send_id_error_not_member": "رقم تعريف المشرف يجب أن يكون عددًا.",
        "confirm_item_add": "<b>تأكيد</b> إضافة {item} إلى {table}؟",
        "item_added": "{item} أضيف إلى {table}!",
        "confirm_item_delete": "<b>تأكيد</b> حذف {item} من {table}؟",
        "item_deleted": "{item} حذف من {table}!"
    },

    "en": {
        "loader_text": "⏳",
        "outdated_text": "...",

        "main_menu": (
            f"{hide_link('https://i.ibb.co/mJVf5Mk/1.png')}"
            "🤖 <b>Welcome!</b>\n\n"
            "To get full access to <b>Alphadhad+</b> channels and services, your wallet must have:\n\n"
            "<blockquote><b>Private Channels:</b>\n{chats}\n"
            "<b>Required Tokens:</b>\n{tokens}</blockquote>\n\n"
            "💡: You can buy the token from DEX by clicking on the ticker ADHD above\n\n"
            "Click on <b>Check access availibility</b> button below, to find out if you'll be admitted!\n\n"            
            "<b>Connected to:</b> {wallet}"
        ),
        "select_language": (
            f"{hide_link('https://i.ibb.co/KhfDvHP/2.png')}"
            "👋 <b>Hello!</b>\n\n"
            "Choose a language:"
        ),
        "change_language": (
            f"{hide_link('https://i.ibb.co/dk5KMzv/3.png')}"
            "<b>Choose a language:</b>"
        ),
        "deny_access": (
            f"{hide_link('https://i.ibb.co/VCKngqF/4.png')}"
            "🚫 <b>Access Denied</b>\n\n"
            "Unfortunately, I did not detect the required tokens in your wallet.\n\n"
            "Don't worry, you can <b>purchase tokens by clicking the buttons</b> below and try again."
        ),
        "allow_access": (
            f"{hide_link('https://i.ibb.co/JyzH4BW/5.png')}"
            "<b>Congratulations! 🥳🎉</b>\n\n"
            "You have access to <b>Alphadhad+</b>\n\n"
            "<b>Click on the Channel name below to join.</b>\n\n" 
            "⚠️ Please note: if you sell or move the required amount of ADHD out of your connected wallet, you will lose your access!"
        ),
        "user_kicked": (
            "User {user} [{wallet}] was kicked from chat!"
        ),

        "connect_wallet": (
            f"<a href='https://ton.org/wallets?locale=en&filters[wallet_features][slug][$in]=dapp-auth&pagination[limit]=-1'>Get a Wallet</a>\n\n"
            "To join <b>Alphadhad+</b>, please connect your <b>{wallet_name}</b> that has the required quantity of <b>ADHD</b>!\n\n"
            "You can select one of the below wallets. Scan with your mobile app wallet:"
        ),
        "connect_wallet_proof_wrong": (
            f"{hide_link('https://i.ibb.co/v4dwwWz/6.png')}"
            "<b>Warning</b>\n\n"
            "The wallet signature is wrong or the connection timeout has expired."
        ),
        "connect_wallet_timeout": (
            f"{hide_link('https://i.ibb.co/tqwj2tZ/7.png')}"
            "<b>Warning</b>\n\n"
            "The connection timeout has expired."
        ),

        "admin_menu": (
            f"{hide_link('https://i.ibb.co/9HkX1y7/main.png')}"
            "<b>Administrator Panel</b>\n\nSelect action:"
        ),
        "chats_menu": (
            f"{hide_link('https://i.ibb.co/9HkX1y7/main.png')}"
            "<b>Private Chats Menu</b>\n\nSelect action:"
        ),
        "chat_info": (
            f"{hide_link('https://i.ibb.co/9HkX1y7/main.png')}"
            "• <b>Private Chat Information</b>\n\n"
            "• <b>ID:</b>\n"
            "<blockquote>{chat_id}</blockquote>\n"
            "• <b>Type:</b>\n"
            "<blockquote>{chat_type}</blockquote>\n"
            "• <b>Name:</b>\n"
            "<blockquote>{chat_name}</blockquote>\n"
            "• <b>Invite Link:</b>\n"
            "<blockquote>{chat_invite_link}</blockquote>\n"
            "• <b>Creation Date:</b>\n"
            "<blockquote>{chat_created_at}</blockquote>"
        ),
        "tokens_menu": (
            f"{hide_link('https://i.ibb.co/9HkX1y7/main.png')}"
            "<b>Tokens Menu</b>\n\nSelect action:"
        ),
        "token_info": (
            f"{hide_link('https://i.ibb.co/9HkX1y7/main.png')}"
            "• <b>Token Information</b>\n\n"
            "• <b>Type:</b>\n"
            "<blockquote>{token_type}</blockquote>\n"
            "• <b>Name:</b>\n"
            "<blockquote>{token_name}</blockquote>\n"
            "• <b>Address:</b>\n"
            "<blockquote>{token_address}</blockquote>\n"
            "• <b>Minimum Amount:</b>\n"
            "<blockquote>{token_min_amount}</blockquote>\n"
            "• <b>Creation Date:</b>\n"
            "<blockquote>{token_created_at}</blockquote>"
        ),
        "token_send_address": "<b>Enter Token Address</b>\n\nOnly NFT collection and Jetton master addresses are allowed:",
        "token_send_address_error": "Invalid token address:\n{}",
        "token_send_address_error_already_exist": "Token with address {address} already exists!",
        "token_send_address_error_not_supported": "Contract {interfaces} is not supported.\nOnly {supported_interfaces} are supported.",
        "token_send_amount": (
            "<b>Token Information</b>:\n\n"
            "• <b>Type:</b>\n"
            "<blockquote>{token_type}</blockquote>\n"
            "• <b>Name:</b>\n"
            "<blockquote>{token_name}</blockquote>\n\n"
            "<b>Enter the minimum token amount</b> to access the private chat:"
        ),
        "token_edit_amount": "<b>Enter the new token amount</b> to access the private chat:",
        "token_send_amount_error": "Invalid token amount!",
        "admins_menu": (
            f"{hide_link('https://i.ibb.co/9HkX1y7/main.png')}"
            "<b>Administrators Menu</b>\n\nSelect action:"
        ),
        "admin_info": (
            f"{hide_link('https://i.ibb.co/9HkX1y7/main.png')}"
            "• <b>Administrator Information</b>\n\n"
            "• <b>ID:</b>\n"
            "<blockquote>{admin_id}</blockquote>\n"
            "• <b>Name:</b>\n"
            "<blockquote>{admin_full_name}</blockquote>\n"
            "• <b>Username:</b>\n"
            "<blockquote>{admin_username}</blockquote>\n"
            "• <b>Creation Date:</b>\n"
            "<blockquote>{admin_created_at}</blockquote>"
        ),
        "admin_send_id": "<b>Enter Administrator ID:</b>",
        "admin_send_id_error": "Invalid ID:\n{}",
        "admin_send_id_error_not_found": "Administrator not found. First, the user needs to start a conversation with the bot.",
        "admin_send_id_error_not_member": "Administrator ID must be a number.",
        "confirm_item_add": "<b>Confirm</b> adding {item} to {table}?",
        "item_added": "{item} added to {table}!",
        "confirm_item_delete": "<b>Confirm</b> deleting {item} from {table}?",
        "item_deleted": "{item} deleted from {table}!"
    }
}
