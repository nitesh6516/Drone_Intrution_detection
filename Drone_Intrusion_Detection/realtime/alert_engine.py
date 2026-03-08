def send_alert(level,attack):

    if level=="CRITICAL":
        print("CRITICAL UAV ATTACK:",attack)

    elif level=="HIGH":
        print("HIGH RISK ATTACK:",attack)

    elif level=="MEDIUM":
        print("Suspicious activity:",attack)

    else:
        print("Normal traffic")