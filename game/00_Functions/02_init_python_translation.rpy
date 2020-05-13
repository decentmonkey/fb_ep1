python early:
    language_dict = json.loads(renpy.file("language_dict.json").read())
#    language_dict = renpy.file("language_dict.json").read()
    language_fields = {None:1, "english":2, "german":3, "spain":4, "chinese":5, "french":6, "turkish":7}

#    open(config.basedir + "/game/update_data.json", "wb").write(str)
    def parse_tstr(str1):
        global item1
        result = re.findall(r'\[(.*?)\]', str1)
#        str1 = str1.replace("{c}", "{")
#        str1 = str1.replace("{/c}", "}")
#        str1 = str1.replace("{", "{c}")
#        str1 = str1.replace("}", "{/c}")
#        str1 = str1.replace("{c{/c}", "{c}")
        for var1 in result:
            var2 = var1
            translateVarFlag = False
            if var2[-2:] == "!t":
                var2 = var2[:-2]
                translateVarFlag = True
            if globals().has_key(var2):
                if translateVarFlag == True:
                    str1 = str1.replace("[" + var1 + "]", str(t__((globals()[var2]))))
                else:
                    str1 = str1.replace("[" + var1 + "]", str(globals()[var2]))
            else:
                if translateVarFlag == True:
                    str1 = str1.replace("[" + var1 + "]", "{c}" + t__(var2) + "{/c}")
                else:
                    str1 = str1.replace("[" + var1 + "]", "{c}" + var2 + "{/c}")
        return str1
    def t_(s):
        return s
#        global _preferences, language_fields, language_dict
#        lang = _preferences.language
#        if language_dict.has_key(s):
#            s = language_dict[s][language_fields[lang]]
#        return parse_tstr(s)
    def t__(s):
        global _preferences, language_fields, language_dict
        lang = _preferences.language
        st = s
        if language_dict.has_key(s):
            st = language_dict[s][language_fields[lang]]
            if st == "":
                st = language_dict[s][language_fields["english"]]
                if st == "":
                    st = s
        return parse_tstr(st)

    def ts__(s):
        global _preferences, language_fields, language_dict
        lang = _preferences.language
        st = s
        if language_dict.has_key(s):
            st = language_dict[s][language_fields[lang]]
            if st == "":
                st = language_dict[s][language_fields["english"]]
                if st == "":
                    st = s
        return parse_tstr(st)
