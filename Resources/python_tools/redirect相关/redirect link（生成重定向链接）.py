def generate_rewrite_rules(rules):
    """
    生成多个 RewriteRule

    参数 rules 是一个列表，每个元素是一个元组，包含源路径和目标路径的对应关系。
    每个元组的格式为 (source_path, target_url)
    """
    rewrite_rules = []

    for source_path, target_url in rules:
        # Escape special characters in source_path and target_url
        escaped_source = source_path.replace('/', '\/').replace('-', '\-').replace('.', '\.')
        escaped_target = target_url.replace('/', '\/').replace(':', '\:').replace('-', '\-').replace('.', '\.')
        # Construct RewriteRule
        rule = f'RewriteRule ^{escaped_source}$ "{escaped_target}" [R=301,L]'
        rewrite_rules.append(rule)

    return rewrite_rules

rules_list = [

('computer-tweaks/2-ways-disable-driver-sigature-enforcement.html', 'https://www.isumsoft.com/computer-tweaks/2-ways-disable-driver-signature-enforcement.html'),
]
# 生成 RewriteRule
generated_rules = generate_rewrite_rules(rules_list)

# 打印生成的 RewriteRule
for rule in generated_rules:
    print(rule)
