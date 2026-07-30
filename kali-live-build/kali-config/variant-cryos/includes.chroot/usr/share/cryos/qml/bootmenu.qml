import QtQuick
import QtQuick.Controls
import QtQuick.Layouts

Window {
    id: bootMenuWindow
    visible: true
    width: 1366
    height: 768
    flags: Qt.Window | Qt.FramelessWindowHint
    color: "#050811"

    property int selectedIndex: 0
    property int timeoutSeconds: 10

    signal bootOptionSelected(string optionName)

    // Background Gradient (Dark Aurora Ice)
    Rectangle {
        anchors.fill: parent
        gradient: Gradient {
            GradientStop { position: 0.0; color: "#060A14" }
            GradientStop { position: 0.5; color: "#0D1527" }
            GradientStop { position: 1.0; color: "#050811" }
        }
    }

    // Main Container
    ColumnLayout {
        anchors.centerIn: parent
        spacing: 20
        width: 620

        // Header Branding
        RowLayout {
            Layout.alignment: Qt.AlignHCenter
            spacing: 12

            Text {
                text: "💎"
                font.pixelSize: 44
            }

            ColumnLayout {
                spacing: 0
                Text {
                    text: "CryOS Polaris"
                    color: "#FFFFFF"
                    font.pixelSize: 28
                    font.bold: true
                    font.letterSpacing: 2
                }
                Text {
                    text: "UEFI Boot Manager v1.0.0"
                    color: "#38BDF8"
                    font.pixelSize: 12
                    font.bold: true
                }
            }
        }

        Item { Layout.preferredHeight: 10 }

        // Boot Menu List Card
        Rectangle {
            Layout.fillWidth: true
            height: 280
            radius: 16
            color: "#CC0F172A"
            border.color: "#33FFFFFF"
            border.width: 1

            ColumnLayout {
                anchors.fill: parent
                anchors.margins: 14
                spacing: 8

                Repeater {
                    id: menuRepeater
                    model: ListModel {
                        ListElement { title: "🚀 CryOS 1.0.0 Polaris (Live System - Normal Boot)"; tag: "Default" }
                        ListElement { title: "🛡 CryOS (Kali Security & Forensic Mode)"; tag: "Security" }
                        ListElement { title: "⚡ CryOS (RAM Persistence Mode - Ultra Fast)"; tag: "RAM" }
                        ListElement { title: "⚙️ UEFI Firmware Settings"; tag: "System" }
                        ListElement { title: "💻 System Memory Diagnostic (Memtest86+)"; tag: "Tools" }
                    }

                    Rectangle {
                        Layout.fillWidth: true
                        height: 44
                        radius: 10
                        color: (index === bootMenuWindow.selectedIndex) ? "#7F2563EB" : (itemMouse.containsMouse ? "#1AFFFFFF" : "transparent")
                        border.color: (index === bootMenuWindow.selectedIndex) ? "#38BDF8" : "transparent"

                        Behavior on color { ColorAnimation { duration: 120 } }

                        MouseArea {
                            id: itemMouse
                            anchors.fill: parent
                            hoverEnabled: true
                            onClicked: {
                                bootMenuWindow.selectedIndex = index
                                bootMenuWindow.bootOptionSelected(model.title)
                            }
                        }

                        RowLayout {
                            anchors.fill: parent
                            anchors.leftMargin: 16
                            anchors.rightMargin: 16
                            spacing: 12

                            Text {
                                text: model.title
                                color: (index === bootMenuWindow.selectedIndex) ? "#FFFFFF" : "#CBD5E1"
                                font.bold: (index === bootMenuWindow.selectedIndex)
                                font.pixelSize: 13
                            }

                            Item { Layout.fillWidth: true }

                            Rectangle {
                                visible: (model.tag !== "")
                                width: tagTxt.implicitWidth + 12
                                height: 20
                                radius: 10
                                color: (index === bootMenuWindow.selectedIndex) ? "#38BDF8" : "#19FFFFFF"

                                Text {
                                    id: tagTxt
                                    anchors.centerIn: parent
                                    text: model.tag
                                    color: (index === bootMenuWindow.selectedIndex) ? "#0F172A" : "#94A3B8"
                                    font.pixelSize: 10
                                    font.bold: true
                                }
                            }
                        }
                    }
                }
            }
        }

        // Timeout Progress Bar & Info Footer
        ColumnLayout {
            Layout.alignment: Qt.AlignHCenter
            spacing: 8

            Text {
                text: "Tự động khởi động mục mặc định sau " + bootMenuWindow.timeoutSeconds + " giây..."
                color: "#64748B"
                font.pixelSize: 11
                Layout.alignment: Qt.AlignHCenter
            }

            Rectangle {
                width: 400
                height: 4
                radius: 2
                color: "#1EFFFFFF"
                Layout.alignment: Qt.AlignHCenter

                Rectangle {
                    width: parent.width * (bootMenuWindow.timeoutSeconds / 10.0)
                    height: parent.height
                    radius: 2
                    color: "#38BDF8"
                    Behavior on width { NumberAnimation { duration: 900 } }
                }
            }

            Text {
                text: "Sử dụng phím  ↑  ↓  để di chuyển | Phím  ENTER  để chọn"
                color: "#475569"
                font.pixelSize: 11
                Layout.alignment: Qt.AlignHCenter
                Layout.topMargin: 4
            }
        }
    }

    // Keyboard Navigation (Up/Down/Enter)
    Item {
        focus: true
        Keys.onUpPressed: {
            if (bootMenuWindow.selectedIndex > 0)
                bootMenuWindow.selectedIndex--
        }
        Keys.onDownPressed: {
            if (bootMenuWindow.selectedIndex < 4)
                bootMenuWindow.selectedIndex++
        }
        Keys.onReturnPressed: {
            bootMenuWindow.bootOptionSelected("Selected Item " + bootMenuWindow.selectedIndex)
        }
    }

    // Timeout countdown timer
    Timer {
        interval: 1000
        running: true
        repeat: true
        onTriggered: {
            if (bootMenuWindow.timeoutSeconds > 0) {
                bootMenuWindow.timeoutSeconds--
            } else {
                running = false
                bootMenuWindow.bootOptionSelected("Default Boot Option")
            }
        }
    }
}
