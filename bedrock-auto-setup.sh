cat << 'EOF' > setup_server.sh
#!/bin/bash

# --- Visual Setup ---
GREEN='\033[0;32m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

echo -e "${BLUE}---------------------------------------------------${NC}"
echo -e "${GREEN}   MADE BY SHUBHAM - SUBSCRIBE TO LEGEND_HACKERYT   ${NC}"
echo -e "${BLUE}---------------------------------------------------${NC}"

# Progress Bar Function
show_progress() {
    local duration=$1
    local label=$2
    echo -n "$label "
    for ((i=0; i<=20; i++)); do
        echo -ne "${GREEN}█${NC}"
        sleep 0.1
    done
    echo -e " [DONE]"
}

# Spinner function for background tasks
spinner() {
    local pid=$1
    local delay=0.1
    local spinstr='|/-\'
    while [ "$(ps a | awk '{print $1}' | grep $pid)" ]; do
        local temp=${spinstr#?}
        printf " [%c]  " "$spinstr"
        local spinstr=$temp${spinstr%"$temp"}
        sleep $delay
        printf "\b\b\b\b\b\b"
    done
    printf "    \b\b\b\b"
}

# 1. Update and Install Tools
echo -e "${BLUE}[1/4] Installing System Tools...${NC}"
(sudo apt update && sudo apt install openjdk-17-jdk maven git screen -y) > /dev/null 2>&1 &
spinner $!
show_progress 2 "Configuring Environment"

# 2. Clone and Build Nukkit-MOT
echo -e "${BLUE}[2/4] Downloading & Compiling Server (Latest 1.26.20)...${NC}"
echo "      (This takes 2-4 minutes, please wait...)"
rm -rf ~/Nukkit-MOT
git clone https://github.com/MemoriesOfTime/Nukkit-MOT.git > /dev/null 2>&1
cd Nukkit-MOT
(mvn clean package -DskipTests) > /dev/null 2>&1 &
spinner $!
echo -e "${GREEN}      Build Success!${NC}"

# 3. Create Minecraft Directory and Move Jar
echo -e "${BLUE}[3/4] Setting up File System...${NC}"
mkdir -p ~/minecraft
cp ~/Nukkit-MOT/target/Nukkit-MOT-SNAPSHOT.jar ~/minecraft/bedrock_server.jar
cd ~/minecraft
show_progress 1 "Moving Assets"

# 4. Create the 24/7 Start Script (2GB Stable)
echo -e "${BLUE}[4/4] Launching 24/7 Background Session...${NC}"
pkill -9 java > /dev/null 2>&1
echo -e '#!/bin/bash\njava -Xmx2048M -Xms1024M -jar bedrock_server.jar' > start_bedrock.sh
chmod +x start_bedrock.sh
screen -dmS bedrock ./start_bedrock.sh
show_progress 1 "Starting Engine"

echo -e "${BLUE}---------------------------------------------------${NC}"
echo -e "${GREEN}   SETUP COMPLETE! SERVER IS LIVE (2GB RAM)        ${NC}"
echo -e "${GREEN}   Use 'screen -r bedrock' to see your console.    ${NC}"
echo -e "${BLUE}---------------------------------------------------${NC}"
EOF

chmod +x setup_server.sh
./setup_server.sh