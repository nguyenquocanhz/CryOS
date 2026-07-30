import QtQuick
import QtQuick.Controls

Window {
    id: bootRoot
    visible: true
    width: 1366
    height: 768
    flags: Qt.Window | Qt.FramelessWindowHint
    color: "#050811"

    property real bootProgress: 0.0
    property string statusText: "Booting CryOS Polaris Kernel 6.6..."

    signal bootFinished()

    // 1. GLOWING CRYSTAL LOGO WITH PULSE ANIMATION
    Column {
        anchors.centerIn: parent
        spacing: 18

        Item {
            width: 130
            height: 130
            anchors.horizontalCenter: parent.horizontalCenter

            // Outer Radial Glow Pulse
            Rectangle {
                id: outerGlow
                anchors.centerIn: parent
                width: 150
                height: 150
                radius: 75
                color: "#2538BDF8"
                scale: 1.0

                SequentialAnimation on scale {
                    running: true
                    loops: Animation.Infinite
                    NumberAnimation { to: 1.3; duration: 1000; easing.type: Easing.InOutQuad }
                    NumberAnimation { to: 1.0; duration: 1000; easing.type: Easing.InOutQuad }
                }

                SequentialAnimation on opacity {
                    running: true
                    loops: Animation.Infinite
                    NumberAnimation { to: 0.9; duration: 1000 }
                    NumberAnimation { to: 0.3; duration: 1000 }
                }
            }

            // Crystal Logo Icon
            Text {
                anchors.centerIn: parent
                text: "💎"
                font.pixelSize: 90
            }
        }

        Text {
            text: "CryOS"
            color: "#FFFFFF"
            font.pixelSize: 42
            font.bold: true
            font.letterSpacing: 4
            anchors.horizontalCenter: parent.horizontalCenter
        }

        Text {
            text: "Polaris Edition - System Boot"
            color: "#38BDF8"
            font.pixelSize: 13
            font.bold: true
            anchors.horizontalCenter: parent.horizontalCenter
        }

        Item { width: 1; height: 28 } // Spacer

        // 2. MACOS STYLE CAPSULE PROGRESS BAR
        Rectangle {
            width: 300
            height: 6
            radius: 3
            color: "#1EFFFFFF"
            anchors.horizontalCenter: parent.horizontalCenter

            Rectangle {
                id: progressBarInner
                width: parent.width * bootRoot.bootProgress
                height: parent.height
                radius: 3
                gradient: Gradient {
                    GradientStop { position: 0.0; color: "#38BDF8" }
                    GradientStop { position: 0.5; color: "#60A5FA" }
                    GradientStop { position: 1.0; color: "#A855F7" }
                }

                Behavior on width {
                    NumberAnimation { duration: 120; easing.type: Easing.OutCubic }
                }
            }
        }

        // Status Text
        Text {
            id: statusLbl
            text: bootRoot.statusText
            color: "#94A3B8"
            font.pixelSize: 12
            font.bold: true
            anchors.horizontalCenter: parent.horizontalCenter
        }
    }

    // 3. CINEMATIC BOOT TIMER
    Timer {
        interval: 40
        running: true
        repeat: true
        onTriggered: {
            bootRoot.bootProgress += 0.008
            if (bootRoot.bootProgress >= 0.20 && bootRoot.bootProgress < 0.45) {
                bootRoot.statusText = "Loading DRM/KMS Graphics & Kali Modules..."
            } else if (bootRoot.bootProgress >= 0.45 && bootRoot.bootProgress < 0.75) {
                bootRoot.statusText = "Starting CryOS Quartz Window Manager..."
            } else if (bootRoot.bootProgress >= 0.75 && bootRoot.bootProgress < 1.0) {
                bootRoot.statusText = "Applying Smooth Flicker-Free Handoff..."
            } else if (bootRoot.bootProgress >= 1.0) {
                running = false
                fadeAnimation.start()
            }
        }
    }

    // Smooth Alpha Handoff Fade-Out Animation
    NumberAnimation {
        id: fadeAnimation
        target: bootRoot
        property: "opacity"
        to: 0.0
        duration: 500
        onFinished: bootRoot.bootFinished()
    }
}
