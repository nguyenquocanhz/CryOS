import QtQuick
import QtQuick.Controls
import QtQuick.Layouts

ApplicationWindow {
    id: rootWindow
    visible: true
    width: 1366
    height: 768
    flags: Qt.Window | Qt.FramelessWindowHint
    title: "CryOS 1.0.0 Polaris (System Service Daemon Integrated)"

    // Background Gradient (Aurora Ice Blue Wallpaper)
    Rectangle {
        anchors.fill: parent
        gradient: Gradient {
            GradientStop { position: 0.0; color: "#090E1A" }
            GradientStop { position: 0.4; color: "#101B35" }
            GradientStop { position: 0.7; color: "#1E1B4B" }
            GradientStop { position: 1.0; color: "#0A1128" }
        }
    }

    // 1. TOP BAR QML
    Rectangle {
        id: topBar
        width: parent.width
        height: 32
        color: "#EF0C1220"
        border.color: "#1EFFFFFF"
        border.width: 1

        RowLayout {
            anchors.fill: parent
            anchors.leftMargin: 12
            anchors.rightMargin: 12
            spacing: 12

            Text {
                text: "💎 CryOS"
                color: "#38BDF8"
                font.bold: true
                font.pixelSize: 14
            }

            Repeater {
                model: ["File", "Edit", "View", "Go", "Window", "Help"]
                Text {
                    text: modelData
                    color: "#E2E8F0"
                    font.pixelSize: 13
                }
            }

            Item { Layout.fillWidth: true }

            // Real-time System Service Stats Badges
            Text {
                text: "⚡ CPU: " + Math.round(cryosService.cpuUsage) + "%"
                color: "#38BDF8"
                font.pixelSize: 11
                font.bold: true
            }

            Text {
                text: "🧠 RAM: " + Math.round(cryosService.ramUsage) + "%"
                color: "#A855F7"
                font.pixelSize: 11
                font.bold: true
            }

            Text { text: "🔋 " + cryosService.batteryPercent + "%"; color: "#FFFFFF"; font.pixelSize: 11; font.bold: true }

            Text {
                text: "🎛"
                color: "#FFFFFF"
                font.pixelSize: 14
                MouseArea {
                    anchors.fill: parent
                    onClicked: controlCenter.visible = !controlCenter.visible
                }
            }

            Text {
                text: "Tue May 27 10:30 AM"
                color: "#F1F5F9"
                font.pixelSize: 12
                font.bold: true
            }

            // Exit System Button
            Text {
                text: "✕"
                color: "#FF5F56"
                font.pixelSize: 14
                font.bold: true
                Layout.leftMargin: 8
                MouseArea {
                    anchors.fill: parent
                    onClicked: Qt.quit()
                }
            }
        }
    }

    // 2. CRYFINDER WINDOW QML
    Rectangle {
        id: finderWindow
        x: 24
        y: 60
        width: 650
        height: 400
        radius: 16
        color: "#F2141E34"
        border.color: "#33FFFFFF"
        border.width: 1

        RowLayout {
            anchors.fill: parent
            spacing: 0

            // Sidebar Left
            Rectangle {
                Layout.preferredWidth: 175
                Layout.fillHeight: true
                color: "#F50F172A"
                border.color: "#19FFFFFF"
                radius: 16

                // Mask top-right and bottom-right sharp corners for rounded sidebar
                Rectangle {
                    anchors.right: parent.right
                    width: 2
                    height: parent.height
                    color: "#19FFFFFF"
                }

                ColumnLayout {
                    anchors.fill: parent
                    anchors.margins: 14
                    spacing: 6

                    // Traffic lights
                    RowLayout {
                        spacing: 8
                        Rectangle {
                            width: 12; height: 12; radius: 6; color: "#FF5F56"
                            MouseArea { anchors.fill: parent; onClicked: finderWindow.visible = false }
                        }
                        Rectangle { width: 12; height: 12; radius: 6; color: "#FFBD2E" }
                        Rectangle { width: 12; height: 12; radius: 6; color: "#27C93F" }
                    }

                    Text { text: "FAVORITES"; color: "#64748B"; font.pixelSize: 10; font.bold: true; Layout.topMargin: 10 }
                    Text { text: "🏠  Home"; color: "#38BDF8"; font.pixelSize: 12; font.bold: true }
                    Text { text: "🖥  Desktop"; color: "#CBD5E1"; font.pixelSize: 12 }
                    Text { text: "📄  Documents"; color: "#CBD5E1"; font.pixelSize: 12 }
                    Text { text: "📥  Downloads"; color: "#CBD5E1"; font.pixelSize: 12 }
                    Text { text: "🖼  Pictures"; color: "#CBD5E1"; font.pixelSize: 12 }

                    Text { text: "LOCATIONS"; color: "#64748B"; font.pixelSize: 10; font.bold: true; Layout.topMargin: 10 }
                    Text { text: "💻  CryOS Drive"; color: "#CBD5E1"; font.pixelSize: 12 }
                    Text { text: "💾  Storage"; color: "#CBD5E1"; font.pixelSize: 12 }

                    Text { text: "TAGS"; color: "#64748B"; font.pixelSize: 10; font.bold: true; Layout.topMargin: 10 }
                    Text { text: "🔴  Work"; color: "#CBD5E1"; font.pixelSize: 12 }
                    Text { text: "🔵  Study"; color: "#CBD5E1"; font.pixelSize: 12 }

                    Item { Layout.fillHeight: true }
                }
            }

            // Right Folder Grid View
            ColumnLayout {
                Layout.fillWidth: true
                Layout.fillHeight: true
                anchors.margins: 16

                RowLayout {
                    Layout.fillWidth: true
                    spacing: 8
                    Text {
                        text: "<  Home"
                        color: "#FFFFFF"
                        font.bold: true
                        font.pixelSize: 14
                    }
                    Item { Layout.fillWidth: true }
                    Text { text: "🎛   ☰   🔍"; color: "#94A3B8"; font.pixelSize: 12 }
                }

                GridView {
                    Layout.fillWidth: true
                    Layout.fillHeight: true
                    Layout.topMargin: 8
                    cellWidth: 110
                    cellHeight: 100
                    model: ListModel {
                        ListElement { fName: "Desktop"; fCount: "12 items"; appCmd: "Finder" }
                        ListElement { fName: "Documents"; fCount: "84 items"; appCmd: "Finder" }
                        ListElement { fName: "Downloads"; fCount: "36 items"; appCmd: "Finder" }
                        ListElement { fName: "Pictures"; fCount: "215 items"; appCmd: "Finder" }
                        ListElement { fName: "Music"; fCount: "47 items"; appCmd: "Finder" }
                        ListElement { fName: "Movies"; fCount: "18 items"; appCmd: "Finder" }
                        ListElement { fName: "Projects"; fCount: "9 items"; appCmd: "VS Code" }
                        ListElement { fName: "Public"; fCount: "3 items"; appCmd: "Finder" }
                    }

                    delegate: Rectangle {
                        width: 100
                        height: 90
                        radius: 12
                        color: folderMouse.containsMouse ? "#3338BDF8" : "#0FFFFFFF"
                        border.color: folderMouse.containsMouse ? "#38BDF8" : "#19FFFFFF"

                        Behavior on color { ColorAnimation { duration: 150 } }

                        MouseArea {
                            id: folderMouse
                            anchors.fill: parent
                            hoverEnabled: true
                            onClicked: cryosService.launchApp(appCmd)
                        }

                        ColumnLayout {
                            anchors.centerIn: parent
                            spacing: 2
                            Text { text: "📁"; font.pixelSize: 32; Layout.alignment: Qt.AlignHCenter }
                            Text { text: fName; color: "#FFFFFF"; font.bold: true; font.pixelSize: 11; Layout.alignment: Qt.AlignHCenter }
                            Text { text: fCount; color: "#64748B"; font.pixelSize: 9; Layout.alignment: Qt.AlignHCenter }
                        }
                    }
                }
            }
        }
    }

    // 3. CRYTERMINAL WINDOW QML
    Rectangle {
        id: terminalWindow
        x: 24
        y: 480
        width: 650
        height: 200
        radius: 14
        color: "#F50A0E1A"
        border.color: "#2DFFFFFF"
        border.width: 1

        ColumnLayout {
            anchors.fill: parent
            anchors.margins: 12
            spacing: 6

            RowLayout {
                spacing: 8
                Rectangle {
                    width: 10; height: 10; radius: 5; color: "#FF5F56"
                    MouseArea { anchors.fill: parent; onClicked: terminalWindow.visible = false }
                }
                Rectangle { width: 10; height: 10; radius: 5; color: "#FFBD2E" }
                Rectangle { width: 10; height: 10; radius: 5; color: "#27C93F" }
                Text { text: "cryos@polaris ~ % neofetch"; color: "#94A3B8"; font.pixelSize: 11; font.bold: true; Layout.leftMargin: 10 }
            }

            Text {
                text: "OS: CryOS 1.0.0 Polaris x86_64 (cryosd App Service Active)\nKernel: 6.6.14-cryos\nDE: CryOS Shell (QML GPU Accelerated)\nWM: CryOS Quartz\nCPU Usage: " + Math.round(cryosService.cpuUsage) + "%\nMemory Usage: " + Math.round(cryosService.ramUsage) + "%\n\ncryos@polaris ~ % █"
                color: "#38BDF8"
                font.family: "Consolas"
                font.pixelSize: 11
                Layout.fillWidth: true
                Layout.fillHeight: true
            }
        }
    }

    // 4. CONTROL CENTER QML PANEL
    Rectangle {
        id: controlCenter
        anchors.right: parent.right
        anchors.top: topBar.bottom
        anchors.rightMargin: 16
        anchors.topMargin: 12
        width: 320
        height: 640
        radius: 20
        color: "#F20F172A"
        border.color: "#2DFFFFFF"
        border.width: 1

        ColumnLayout {
            anchors.fill: parent
            anchors.margins: 14
            spacing: 12

            Text { text: "Control Center & Notifications"; color: "#38BDF8"; font.bold: true; font.pixelSize: 13 }

            // Toggles Grid Connected to CryOS App Service
            GridLayout {
                columns: 2
                columnSpacing: 8
                rowSpacing: 8
                Layout.fillWidth: true

                // Wi-Fi Card Toggle
                Rectangle {
                    Layout.fillWidth: true
                    height: 48
                    radius: 12
                    color: cryosService.wifiEnabled ? "#7F2563EB" : "#14FFFFFF"
                    border.color: cryosService.wifiEnabled ? "#3B82F6" : "#1FFFFFFF"

                    MouseArea {
                        anchors.fill: parent
                        onClicked: cryosService.toggleWifi()
                    }

                    RowLayout {
                        anchors.fill: parent
                        anchors.margins: 8
                        spacing: 8
                        Text { text: "📶"; font.pixelSize: 18 }
                        ColumnLayout {
                            spacing: 0
                            Text { text: "Wi-Fi"; color: "#FFFFFF"; font.bold: true; font.pixelSize: 10 }
                            Text { text: cryosService.wifiEnabled ? cryosService.wifiSsid : "Off"; color: "#94A3B8"; font.pixelSize: 9 }
                        }
                    }
                }

                // Bluetooth Card Toggle
                Rectangle {
                    Layout.fillWidth: true
                    height: 48
                    radius: 12
                    color: cryosService.bluetoothEnabled ? "#7F2563EB" : "#14FFFFFF"
                    border.color: cryosService.bluetoothEnabled ? "#3B82F6" : "#1FFFFFFF"

                    MouseArea {
                        anchors.fill: parent
                        onClicked: cryosService.toggleBluetooth()
                    }

                    RowLayout {
                        anchors.fill: parent
                        anchors.margins: 8
                        spacing: 8
                        Text { text: "🎧"; font.pixelSize: 18 }
                        ColumnLayout {
                            spacing: 0
                            Text { text: "Bluetooth"; color: "#FFFFFF"; font.bold: true; font.pixelSize: 10 }
                            Text { text: cryosService.bluetoothEnabled ? "On" : "Off"; color: "#94A3B8"; font.pixelSize: 9 }
                        }
                    }
                }

                // AirDrop Card
                Rectangle {
                    Layout.fillWidth: true
                    height: 48
                    radius: 12
                    color: "#7F2563EB"
                    border.color: "#3B82F6"

                    RowLayout {
                        anchors.fill: parent
                        anchors.margins: 8
                        spacing: 8
                        Text { text: "📡"; font.pixelSize: 18 }
                        ColumnLayout {
                            spacing: 0
                            Text { text: "AirDrop"; color: "#FFFFFF"; font.bold: true; font.pixelSize: 10 }
                            Text { text: "Everyone"; color: "#94A3B8"; font.pixelSize: 9 }
                        }
                    }
                }

                // Do Not Disturb Card
                Rectangle {
                    Layout.fillWidth: true
                    height: 48
                    radius: 12
                    color: "#14FFFFFF"
                    border.color: "#1FFFFFFF"

                    RowLayout {
                        anchors.fill: parent
                        anchors.margins: 8
                        spacing: 8
                        Text { text: "🌙"; font.pixelSize: 18 }
                        ColumnLayout {
                            spacing: 0
                            Text { text: "Do Not Disturb"; color: "#FFFFFF"; font.bold: true; font.pixelSize: 10 }
                            Text { text: "Off"; color: "#94A3B8"; font.pixelSize: 9 }
                        }
                    }
                }
            }

            // Sliders Connected to Service
            Rectangle {
                Layout.fillWidth: true
                height: 40
                radius: 10
                color: "#0FFFFFFF"
                RowLayout {
                    anchors.fill: parent
                    anchors.margins: 8
                    Text { text: "Display"; color: "#94A3B8"; font.pixelSize: 10 }
                    Slider {
                        value: cryosService.brightnessLevel / 100.0
                        Layout.fillWidth: true
                        onMoved: cryosService.setBrightness(value * 100)
                    }
                }
            }

            Rectangle {
                Layout.fillWidth: true
                height: 40
                radius: 10
                color: "#0FFFFFFF"
                RowLayout {
                    anchors.fill: parent
                    anchors.margins: 8
                    Text { text: "Sound"; color: "#94A3B8"; font.pixelSize: 10 }
                    Slider {
                        value: cryosService.volumeLevel / 100.0
                        Layout.fillWidth: true
                        onMoved: cryosService.setVolume(value * 100)
                    }
                }
            }

            // Notifications
            Text { text: "Notifications"; color: "#94A3B8"; font.bold: true; font.pixelSize: 11; Layout.topMargin: 6 }
            
            Rectangle {
                Layout.fillWidth: true
                height: 55
                radius: 10
                color: "#0FFFFFFF"
                ColumnLayout {
                    anchors.fill: parent
                    anchors.margins: 8
                    Text { text: "💎 CryOS Service (now)"; color: "#38BDF8"; font.bold: true; font.pixelSize: 10 }
                    Text { text: "cryosd App Service is active and monitoring."; color: "#CBD5E1"; font.pixelSize: 9 }
                }
            }

            Item { Layout.fillHeight: true }
        }
    }

    // 5. FLOATING BOTTOM DOCK CONNECTED TO APP LAUNCHER SERVICE
    Rectangle {
        id: dockPill
        anchors.bottom: parent.bottom
        anchors.horizontalCenter: parent.horizontalCenter
        anchors.bottomMargin: 12
        height: 68
        width: dockRow.implicitWidth + 28
        radius: 22
        color: "#F00F172A"
        border.color: "#33FFFFFF"
        border.width: 1

        RowLayout {
            id: dockRow
            anchors.centerIn: parent
            spacing: 8

            Repeater {
                model: [
                    { icon: "🔷", appCmd: "Finder", active: false },
                    { icon: "🎛", appCmd: "Browser", active: false },
                    { icon: "💎", appCmd: "VS Code", active: true },
                    { icon: "✉️", appCmd: "Browser", active: false },
                    { icon: "📅", appCmd: "Finder", active: false },
                    { icon: "📝", appCmd: "VS Code", active: false },
                    { icon: "🖼", appCmd: "Finder", active: false },
                    { icon: "💻", appCmd: "Terminal", active: true },
                    { icon: "⚙️", appCmd: "Finder", active: false },
                    { icon: "🗑", appCmd: "Finder", active: false }
                ]

                ColumnLayout {
                    spacing: 2

                    Rectangle {
                        width: 46
                        height: 46
                        radius: 12
                        color: dockItemMouse.containsMouse ? "#33FFFFFF" : "transparent"
                        scale: dockItemMouse.containsMouse ? 1.25 : 1.0

                        Behavior on scale { ScaleAnimator { duration: 120; easing.type: Easing.OutBack } }

                        Text {
                            anchors.centerIn: parent
                            text: modelData.icon
                            font.pixelSize: 26
                        }

                        MouseArea {
                            id: dockItemMouse
                            anchors.fill: parent
                            hoverEnabled: true
                            onClicked: cryosService.launchApp(modelData.appCmd)
                        }
                    }

                    Text {
                        text: "•"
                        color: modelData.active ? "#FFFFFF" : "transparent"
                        font.pixelSize: 12
                        font.bold: true
                        Layout.alignment: Qt.AlignHCenter
                    }
                }
            }
        }
    }
}
