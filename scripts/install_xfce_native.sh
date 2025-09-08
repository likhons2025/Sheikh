#!/bin/bash
#
# Sheikh Phase 1: Mobile Workstation Environment Setup
#
# This script transforms a standard Termux installation into a full-featured
# Debian development environment with a graphical XFCE desktop, audio support,
# and a container engine (Podman).
#
# Author: Jules for the Sheikh Project
# Date: 2025-09-08

set -e # Exit immediately if a command exits with a non-zero status.

# --- Helper Functions for Logging ---
info() {
    echo "[INFO] $1"
}

success() {
    echo "✅ [SUCCESS] $1"
}

# --- Main Installation Logic ---

main() {
    info "Starting Sheikh Phase 1: Mobile Workstation Setup"

    # --- 1. Install Termux Host Dependencies ---
    info "Updating Termux packages and installing host dependencies..."
    pkg update -y && pkg upgrade -y
    pkg install -y proot-distro pulseaudio termux-x11-nightly x11-repo
    success "Termux host dependencies installed."

    # --- 2. Install Debian Root Filesystem ---
    info "Installing Debian proot environment. This may take a while..."
    # Check if Debian is already installed to avoid errors
    if proot-distro list | grep -q "debian"; then
        info "Debian is already installed. Skipping installation."
    else
        proot-distro install debian
        success "Debian root filesystem installed."
    fi

    # --- 3. Install Debian Guest Packages and Configure Environment ---
    info "Logging into Debian to install guest packages and configure the environment..."

    # Use a heredoc to execute a block of commands within the Debian proot
    proot-distro login debian -- bash -c '
        set -e
        echo "[DEBIAN-INFO] Updating APT repositories..."
        apt-get update && apt-get upgrade -y

        echo "[DEBIAN-INFO] Installing XFCE desktop, audio, and core utilities..."
        # Use --no-install-recommends to keep the installation minimal
        apt-get install -y --no-install-recommends \
            xfce4 \
            xfce4-goodies \
            xfce4-terminal \
            dbus-x11 \
            pulseaudio \
            git \
            nano \
            htop

        echo "[DEBIAN-INFO] Installing Podman container engine..."
        apt-get install -y podman

        echo "[DEBIAN-INFO] Configuring PulseAudio to connect to Termux host..."
        # This allows audio from the Debian guest to play through the Android host
        echo "default-server = 127.0.0.1" > /etc/pulse/client.conf

        echo "[DEBIAN-SUCCESS] Guest environment setup is complete."
    '
    success "Debian guest environment has been configured."

    # --- 4. Create Launcher Script ---
    info "Creating a launcher script 'start-sheikh.sh'..."
    cat > ~/start-sheikh.sh <<- EOM
#!/bin/bash
# Launcher for the Sheikh XFCE Environment

# Start PulseAudio on the Termux host
pulseaudio --start --exit-idle-time=-1
pacmd load-module module-native-protocol-tcp auth-ip-acl=127.0.0.1 auth-anonymous=1

# Login to Debian and start the XFCE session
echo "Launching XFCE Desktop Environment..."
echo "Please connect using your Termux-X11 client."

proot-distro login debian --user root --shared-tmp -- \
  env DISPLAY=:0 \
  dbus-launch --exit-with-session xfce4-session
EOM

    chmod +x ~/start-sheikh.sh
    success "Launcher script created at ~/start-sheikh.sh"

    # --- Final Instructions ---
    echo ""
    info "------------------------------------------------------------"
    info "Sheikh Environment Installation Complete!"
    info "To start your graphical development environment:"
    info "1. Open the Termux-X11 application."
    info "2. In a new Termux session, run the command: ./start-sheikh.sh"
    info "------------------------------------------------------------"
}

# --- Run the main function ---
main
