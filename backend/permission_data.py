
# PermissionWise
# Android Permission Knowledge Base

PERMISSIONS = {

    "CAMERA": {
        "name": "Camera",
        "category": "Device Hardware",
        "description": "Allows an app to access the device camera.",
        "possible_use": "Taking photos, recording videos or scanning QR codes.",
        "privacy_concern": "Camera access may expose visual information about the user and their surroundings.",
        "user_advice": "Check whether camera access is necessary for the app's main features."
    },

    "RECORD_AUDIO": {
        "name": "Microphone",
        "category": "Device Hardware",
        "description": "Allows an app to capture audio using the device microphone.",
        "possible_use": "Voice messages, calls, voice search or audio recording.",
        "privacy_concern": "Audio can contain conversations and other sensitive information.",
        "user_advice": "Allow microphone access only when it is needed."
    },

    "ACCESS_FINE_LOCATION": {
        "name": "Precise Location",
        "category": "Location",
        "description": "Allows an app to request precise device location.",
        "possible_use": "Navigation, maps or location-based services.",
        "privacy_concern": "Precise location can reveal where a person lives, works or travels.",
        "user_advice": "Check whether approximate location would be sufficient."
    },

    "ACCESS_COARSE_LOCATION": {
        "name": "Approximate Location",
        "category": "Location",
        "description": "Allows an app to request approximate device location.",
        "possible_use": "Local weather, nearby services or regional recommendations.",
        "privacy_concern": "Location information can still reveal patterns about a person's movements.",
        "user_advice": "Consider whether the app genuinely needs location access."
    },

    "READ_CONTACTS": {
        "name": "Read Contacts",
        "category": "Personal Information",
        "description": "Allows an app to read contacts stored on the device.",
        "possible_use": "Finding friends, sharing content or contact synchronisation.",
        "privacy_concern": "Contacts may contain names, phone numbers and other personal information about you and others.",
        "user_advice": "Check whether contact access is essential to the feature you want to use."
    },
    
    "BLUETOOTH_SCAN": {
        "name": "Bluetooth Scan",
        "category": "Nearby Devices",
        "description": "Allows an app to discover nearby Bluetooth devices.",
        "possible_use": "Finding smartwatches, headphones and other nearby devices.",
        "privacy_concern": "Nearby device discovery can reveal information about the user's surroundings. In some circumstances, Bluetooth scanning can also reveal location.",
        "user_advice": "Check whether nearby device discovery is necessary for the app.",        "introduced_api": 31,
        "protection_level": "dangerous",
        "source": "https://developer.android.com/reference/android/Manifest.permission#BLUETOOTH_SCAN"
    },

    "BLUETOOTH_CONNECT": {
        "name": "Bluetooth Connect",
        "category": "Nearby Devices",
        "description": "Allows an app to connect to paired Bluetooth devices.",
        "possible_use": "Connecting to headphones, speakers and wearable devices.",
        "privacy_concern": "Bluetooth interactions may expose information about connected devices.",
        "user_advice": "Check which connected devices the app needs to communicate with.",        "introduced_api": 31,
        "protection_level": "dangerous",
        "source": "https://developer.android.com/reference/android/Manifest.permission#BLUETOOTH_CONNECT"
    },

    "BLUETOOTH_ADVERTISE": {
        "name": "Bluetooth Advertise",
        "category": "Nearby Devices",
        "description": "Allows an app to make the device discoverable to nearby Bluetooth devices.",
        "possible_use": "Broadcasting the device's presence to nearby devices.",
        "privacy_concern": "Making a device discoverable may expose its presence to nearby devices.",
        "user_advice": "Check whether the app genuinely needs to make your device discoverable.",        "introduced_api": 31,
        "protection_level": "dangerous",
        "source": "https://developer.android.com/reference/android/Manifest.permission#BLUETOOTH_ADVERTISE"
    },

    "READ_CALENDAR": {
        "name": "Read Calendar",
        "category": "Personal Information",
        "description": "Allows an app to read calendar data.",
        "possible_use": "Displaying events, scheduling meetings and managing appointments.",
        "privacy_concern": "Calendar entries may reveal personal schedules, meetings and activities.",
        "user_advice": "Check whether calendar access is necessary for the app's features.",        "introduced_api": 1,
        "protection_level": "dangerous",
        "source": "https://developer.android.com/reference/android/Manifest.permission#READ_CALENDAR"
    },

    "READ_PHONE_STATE": {
        "name": "Read Phone State",
        "category": "Phone Information",
        "description": "Allows an app to read certain phone state and cellular network information.",
        "possible_use": "Telephony-related features and understanding phone connectivity.",
        "privacy_concern": "Some phone-state information may reveal details about device usage and connectivity.",
        "user_advice": "Check why the application needs access to phone-state information.",         "user_advice": "Check whether the app genuinely needs phone-state information.",
        "introduced_api": 1,
        "protection_level": "dangerous",
        "source": "https://developer.android.com/reference/android/Manifest.permission#READ_PHONE_STATE"
    },
    

    "POST_NOTIFICATIONS": {
        "name": "Post Notifications",
        "category": "Notifications",
        "description": "Allows an app to request permission to send non-exempt notifications on Android 13 and later.",
        "possible_use": "Sending messages, reminders, alerts and updates.",
        "privacy_concern": "Notifications may reveal sensitive information on the lock screen or notification panel.",
        "user_advice": "Consider whether the app's notifications are useful and appropriate.",        "introduced_api": 33,
        "protection_level": "dangerous",
        "source": "https://developer.android.com/reference/android/Manifest.permission#POST_NOTIFICATIONS"
    },

    "READ_MEDIA_IMAGES": {
        "name": "Read Media Images",
        "category": "Photos and Media",
        "description": "Allows an app to read image files from shared storage.",
        "possible_use": "Selecting, displaying and processing photos.",
        "privacy_concern": "Images may contain personal, sensitive or identifying information.",
        "user_advice": "Consider whether selecting specific photos through the photo picker is sufficient.",        "introduced_api": 33,
        "protection_level": "dangerous",
        "source": "https://developer.android.com/reference/android/Manifest.permission#READ_MEDIA_IMAGES"
    },

    "READ_MEDIA_VIDEO": {
        "name": "Read Media Video",
        "category": "Photos and Media",
        "description": "Allows an app to read video files from shared storage.",
        "possible_use": "Selecting, displaying and editing videos.",
        "privacy_concern": "Videos may contain personal activities, people and location-related information.",
        "user_advice": "Check whether the app needs broad video access or only selected videos.",        "introduced_api": 33,
        "protection_level": "dangerous",
        "source": "https://developer.android.com/reference/android/Manifest.permission#READ_MEDIA_VIDEO"
    },
    "READ_MEDIA_VISUAL_USER_SELECTED": {
        "name": "Read Selected Media",
        "category": "Photos and Media",
        "description": "Allows an app to access photos and videos specifically selected by the user.",
        "possible_use": "Uploading selected photos or videos without requiring broad media access.",
        "privacy_concern": "Selected media may still contain personal or sensitive information.",
        "user_advice": "Prefer granting access only to the photos and videos needed by the app.",
        "introduced_api": 34,
        "protection_level": "dangerous",
        "source": "https://developer.android.com/reference/android/Manifest.permission#READ_MEDIA_VISUAL_USER_SELECTED"
    },

}


def get_permission(permission_name):

    permission = PERMISSIONS.get(permission_name)

    if permission is None:
        return None

    return permission


def analyse_permissions(permission_list):

    results = []
    unknown_permissions = []
    duplicate_permissions = []
    seen_permissions = set()

    for permission_name in permission_list:

        permission_name = permission_name.strip().upper()

        if not permission_name:
            continue

        if permission_name in seen_permissions:
            duplicate_permissions.append(permission_name)
            continue

        seen_permissions.add(permission_name)

        permission = get_permission(permission_name)

        if permission is not None:
            results.append(permission)
        else:
            unknown_permissions.append(permission_name)

    return results, unknown_permissions, duplicate_permissions

