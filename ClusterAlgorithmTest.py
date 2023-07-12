import nltk
nltk.download('punkt')
from textblob.classifiers import NaiveBayesClassifier

# Define the job categories
categories = [('IT-Software development', ['Software development', 'Programming', 'Software engineering', 'Software design',  'Mobile app development', 'Agile methodologies', 'Object-oriented programming', 'Front-end development', 'Back-end development', 'Full-stack development', 'Software testing', 'Debugging', 'Version control', 'Software architecture', 'Database management', 'API development', 'Code optimization', 'Software deployment', 'Continuous integration']),
('IT-Web Development', ['Web development', 'Front-end development', 'Back-end development', 'HTML', 'CSS', 'JavaScript', 'Responsive design', 'UI/UX design', 'Web frameworks', 'CMS', 'Version control', 'API integration', 'Cross-browser compatibility', 'Web performance optimization', 'Website maintenance', 'Debugging', 'Testing', 'SEO', 'Web security', 'Agile methodologies']),
('IT-Data Science', ['Data science', 'Machine learning', 'Data analysis', 'Statistical modeling', 'Data visualization', 'Python', 'R', 'SQL', 'Data mining', 'Predictive modeling', 'Data manipulation', 'Data preprocessing', 'Data wrangling', 'Feature engineering', 'Supervised learning', 'Unsupervised learning', 'Deep learning', 'Natural language processing', 'Big data', 'Data storytelling']),
('IT-Cybersecurity', ['Cybersecurity', 'Information security', 'Network security', 'Vulnerability assessment', 'Penetration testing', 'Security monitoring', 'Incident response', 'Security policies', 'Security audits', 'Risk assessment', 'Firewalls', 'Intrusion detection systems', 'Encryption', 'Authentication', 'Security frameworks', 'Security awareness', 'Threat intelligence', 'Security operations', 'Security architecture', 'Compliance']),
('IT-Network Administration', ['Web development', 'HTML', 'CSS', 'JavaScript', 'Front-end', 'Back-end', 'Responsive design', 'API integration', 'UI/UX', 'Cross-browser compatibility', 'Version control', 'Responsive frameworks', 'RESTful services', 'PHP', 'Python', 'Node.js', 'React', 'Angular', 'Vue.js', 'MySQL', 'MongoDB']),
('IT-IT Support', ['Network administration', 'Network infrastructure', 'Routing and switching', 'Network protocols', 'TCP/IP', 'DNS', 'DHCP', 'Firewalls', 'VPN', 'LAN', 'WAN', 'Network security', 'Network monitoring', 'Troubleshooting', 'Network performance optimization', 'Network documentation', 'Network backups', 'Patch management', 'Network upgrades', 'Network capacity planning']),
('Business and Finance-Accounting', ['Accounting', 'Financial statements', 'Bookkeeping', 'Financial analysis', 'Budgeting', 'Taxation', 'Auditing', 'Payroll', 'Financial reporting', 'Accounts payable', 'Accounts receivable', 'General ledger', 'Cost accounting', 'Financial forecasting', 'Financial controls', 'Accounting software', 'GAAP', 'IFRS', 'Financial regulations', 'Risk management']),
('Business and Finance:Finance', ['Finance', 'Financial planning', 'Investment analysis', 'Financial modeling', 'Capital budgeting', 'Risk management', 'Financial reporting', 'Financial analysis', 'Corporate finance', 'Financial markets', 'Financial strategies', 'Asset management', 'Portfolio management', 'Financial forecasting', 'Valuation', 'Financial ratios', 'Financial regulations', 'Cash flow management', 'Financial decision-making', 'Financial software']),
('Business and Finance:Marketing', ['Marketing', 'Market research', 'Marketing strategy', 'Digital marketing', 'Social media marketing', 'Content marketing', 'Brand management', 'Marketing campaigns', 'Advertising', 'Email marketing', 'SEO', 'SEM', 'Marketing analytics', 'Consumer behavior', 'Product management', 'Marketing communications', 'Marketing automation', 'Market segmentation', 'Marketing ROI', 'Customer acquisition']),
('Business and Finance:Human Resources', ['Human resources', 'Employee relations', 'Recruitment', 'Talent acquisition', 'Performance management', 'Training and development', 'Compensation and benefits', 'HR policies', 'Employee engagement', 'HRIS', 'Labor laws', 'HR compliance', 'Organizational development', 'Succession planning', 'Workforce planning', 'Employee retention', 'Onboarding', 'HR metrics', 'Diversity and inclusion', 'HR software']),
('Business and Finance:Sales', ['Sales', 'Business development', 'Sales strategy', 'Prospecting', 'Negotiation', 'Client relationship management', 'Sales forecasting', 'Account management', 'Lead generation', 'Sales presentations', 'Closing deals', 'Sales targets', 'Sales process', 'CRM', 'Customer acquisition', 'Customer retention', 'Sales techniques', 'Consultative selling', 'Sales analytics', 'Sales management']),
('Business and Finance:Management', ['Management', 'Leadership', 'Team management', 'Strategic planning', 'Decision-making', 'Project management', 'Performance management', 'Change management', 'Organizational development', 'Budget management', 'Problem-solving', 'Conflict resolution', 'Communication skills', 'Team building', 'Stakeholder management', 'Time management', 'Goal setting', 'Delegation', 'Performance evaluation', 'Business acumen']),
('Education:Teaching', ['Teaching', 'Classroom management', 'Lesson planning', 'Curriculum development', 'Instructional techniques', 'Student assessment', 'Differentiated instruction', 'Educational technology', 'Student engagement', 'Teaching strategies', 'Classroom activities', 'Student-centered learning', 'Pedagogy', 'Special needs education', 'Inclusive education', 'Assessment strategies', 'Subject knowledge', 'Learning objectives', 'Education standards', 'Student motivation']),
('Education:Administration', ['Administration', 'Administrative tasks', 'Office management', 'Data management', 'Scheduling', 'Records management', 'Budget management', 'Report generation', 'Meeting coordination', 'Documentation', 'Policy development', 'Project coordination', 'Administrative support', 'Time management', 'Communication skills', 'Organizational skills', 'Decision-making', 'Problem-solving', 'Attention to detail', 'Team collaboration']),
('Education:Research', ['Research', 'Research methodology', 'Data analysis', 'Literature review', 'Qualitative research', 'Quantitative research', 'Experimental design', 'Data collection', 'Statistical analysis', 'Research ethics', 'Research proposal', 'Research findings', 'Data interpretation', 'Research publication', 'Research collaboration', 'Research presentation', 'Research funding', 'Research impact', 'Critical thinking', 'Research skills']),
('Education:Curriculum Development', ['Curriculum development', 'Educational planning', 'Instructional design', 'Learning objectives', 'Curriculum mapping', 'Educational standards', 'Assessment strategies', 'Learning materials', 'Curriculum alignment', 'Curriculum evaluation', 'Curriculum review', 'Curriculum implementation', 'Curriculum modifications', 'Curriculum assessment', 'Curriculum documentation', 'Curriculum enhancement', 'Curriculum coordination', 'Curriculum analysis', 'Curriculum innovation', 'Curriculum adaptation']),
('Education:Counseling', ['Counseling', 'Individual counseling', 'Group counseling', 'Counseling techniques', 'Mental health counseling', 'Emotional support', 'Crisis intervention', 'Assessment and evaluation', 'Behavioral interventions', 'Counseling theories', 'Psychoeducation', 'Career counseling', 'School counseling', 'Student counseling', 'Guidance counseling', 'Solution-focused counseling', 'Counseling ethics', 'Counseling skills', 'Therapeutic relationship', 'Counseling interventions']),
('Education:Special Education', ['Special education', 'Individualized education plans (IEPs)', 'Inclusion', 'Differentiated instruction', 'Special needs assessment', 'Behavior management', 'Learning disabilities', 'Autism spectrum disorders', 'Intellectual disabilities', 'Emotional and behavioral disorders', 'Speech and language impairments', 'Adaptive behavior skills', 'Special education laws', 'Collaborative teaching', 'IEP meetings', 'Supportive interventions', 'Transition planning', 'Assistive technology', 'Parent collaboration', 'Inclusive practices']),

]
''' 
    ('Data Scientist', ['Machine learning', 'statistics', 'programming', 'data analysis', 'data visualization','Data science', 'Machine learning', 'Statistical analysis', 'Data mining', 'Predictive modeling', 'Big data', 'Data visualization', 'Python', 'R programming', 'SQL', 'Deep learning', 'Natural language processing', 'AI algorithms', 'Feature engineering', 'Hadoop', 'Spark', 'Data preprocessing', 'Data wrangling', 'Experiment design', 'Model evaluation']),
    ('Web Developer', ['Web development', 'HTML', 'CSS', 'JavaScript', 'Front-end', 'Back-end', 'Responsive design', 'API integration', 'UI/UX', 'Cross-browser compatibility', 'Version control', 'Responsive frameworks', 'RESTful services', 'PHP', 'Python', 'Node.js', 'React', 'Angular', 'Vue.js', 'MySQL', 'MongoDB']),
    ('Marketing Coordinator', ['Marketing coordination', 'Campaign management', 'Digital marketing', 'Social media management', 'Content creation', 'Email marketing', 'Marketing analytics', 'Market research', 'Brand management', 'Event coordination', 'Project management', 'Copywriting', 'SEO optimization', 'Google Analytics', 'CRM software', 'Marketing collateral', 'Lead generation', 'Campaign tracking', 'Advertising', 'Public relations']),
    ('Project Manager', ['Project management', 'Team leadership', 'Agile methodology', 'Scrum', 'Project planning', 'Risk management', 'Stakeholder management', 'Budgeting', 'Resource allocation', 'Communication', 'Problem-solving', 'Project coordination', 'Quality assurance', 'Milestone tracking', 'Project documentation', 'Scope management', 'Change management', 'Project scheduling', 'Project delivery', 'Client management']),
    ('Sales Representative', ['Sales', 'Prospecting', 'Negotiation', 'Relationship building', 'Client acquisition', 'CRM', 'Cold calling', 'Closing deals', 'Sales targets', 'Presentation skills', 'Client management', 'Lead generation', 'Account management', 'Sales forecasting', 'Sales techniques', 'Networking', 'Customer service', 'Business development', 'Consultative selling', 'Sales process']),
    ('Human Resources Generalist',['Human resources', 'Recruitment', 'Employee relations', 'Performance management', 'HR policies', 'Onboarding', 'Benefits administration', 'Training and development', 'Employee engagement', 'HRIS', 'Compliance', 'Policy development', 'Conflict resolution', 'Talent acquisition', 'Compensation management', 'HR programs', 'Organizational development', 'HR metrics', 'Employment law', 'Workforce planning']),
    ('Financial Analyst', ['Financial analysis', 'Forecasting', 'Budgeting', 'Financial modeling', 'Investment analysis', 'Risk assessment', 'Data analysis', 'Financial reporting', 'Variance analysis', 'Cost analysis', 'Cash flow management', 'Financial planning', 'Valuation', 'Budget variance', 'Profitability analysis', 'Financial statements', 'Trend analysis', 'Financial projections', 'Capital expenditure', 'Cost control']),
    ('Software Engineer',['Software engineering', 'Programming', 'Object-oriented programming', 'Software development', 'Algorithm design', 'Debugging', 'Testing', 'Coding', 'Software architecture', 'Version control', 'Agile methodology', 'Problem-solving', 'Database management', 'Web development', 'Full-stack development', 'Front-end', 'Back-end', 'Mobile app development', 'API integration', 'Software documentation']),
    ('Accountant', ['Accounting', 'Financial statements', 'Bookkeeping', 'Financial analysis', 'Taxation', 'Budgeting', 'Auditing', 'Financial reporting', 'General ledger', 'Payroll management', 'Accounts payable', 'Accounts receivable', 'Financial forecasting', 'Cost analysis', 'Internal controls', 'Financial regulations', 'Cash flow management', 'Tax planning', 'Financial systems', 'Financial modeling']),
    ('Copywriter', ['Copywriting', 'Content creation', 'Advertising', 'Marketing', 'Creative writing', 'Brand messaging', 'Proofreading', 'Editing', 'Content strategy', 'SEO optimization', 'Social media', 'Copy editing', 'Marketing campaigns', 'Content marketing', 'Branding', 'Headline writing', 'Storytelling', 'Persuasive writing', 'Print media', 'Digital content']),
    ('UX Designer', ['UX design', 'User experience', 'User interface', 'Wireframing', 'Prototyping', 'Usability testing', 'User research', 'Information architecture', 'Interaction design', 'Visual design', 'Responsive design', 'User-centered design', 'Design thinking', 'UI/UX', 'Persona development', 'User flows', 'User journey mapping', 'Accessibility', 'Mobile design', 'Web design']),
    ('Customer Service Representative',['Customer service', 'Customer support', 'Communication', 'Problem-solving', 'Product knowledge', 'Conflict resolution', 'Call center', 'Customer satisfaction', 'Customer relationship management', 'Issue escalation', 'Troubleshooting', 'Service inquiries', 'Complaint handling', 'Order management', 'Customer retention', 'Cross-selling', 'Up-selling', 'Multitasking', 'Empathy', 'Time management']),
    ('IT Support',['IT support', 'Technical support', 'Troubleshooting', 'Hardware', 'Software', 'Network support', 'Helpdesk', 'System administration', 'Incident management', 'Ticketing system', 'Remote support', 'Customer service', 'Problem-solving', 'IT infrastructure', 'Desktop support', 'Software installation', 'User training', 'Documentation', 'ITIL', 'IT security']),
    ('Supply Chain Analyst',['Supply chain', 'Logistics', 'Inventory management', 'Demand forecasting', 'Data analysis', 'Process improvement', 'Supply chain optimization', 'Supplier management', 'Supply chain planning', 'Procurement', 'Supply chain analytics', 'Vendor performance', 'Supply chain metrics', 'Risk management', 'Forecasting models', 'Operations management', 'Supply chain software', 'Cost reduction', 'Lead time analysis', 'Continuous improvement']),
    ('Social Media Manager',['Social media', 'Social media management', 'Content creation', 'Social media strategy', 'Community management', 'Digital marketing', 'Content marketing', 'Social media campaigns', 'Audience engagement', 'Social media analytics', 'Brand management', 'Influencer marketing', 'Content scheduling', 'Social media platforms', 'Campaign optimization', 'Social media advertising', 'Performance tracking', 'Social media trends', 'Customer engagement', 'Social media metrics']),
    ('Business Analyst',['Business analysis', 'Requirements gathering', 'Data analysis', 'Process improvement', 'Business process modeling', 'Stakeholder management', 'Gap analysis', 'Business requirements', 'Business intelligence', 'Requirement documentation', 'Data modeling', 'Process mapping', 'Business process reengineering', 'Agile methodology', 'Business systems', 'Data visualization', 'User stories', 'Root cause analysis', 'Business strategy', 'Problem-solving']),
    ('Executive Assistant',['Executive assistant', 'Calendar management', 'Meeting coordination', 'Travel arrangements', 'Email management', 'Document preparation', 'Administrative support', 'Project coordination', 'Time management', 'Event planning', 'Executive support', 'Presentation preparation', 'Communication', 'Confidentiality', 'Organization', 'Decision-making support', 'Correspondence management', 'Problem-solving', 'Prioritization', 'Attention to detail']),
    ('Mechanical Engineer', ['Mechanical engineering', 'Design', 'CAD', 'Product development', 'Mechanical design', 'Manufacturing', 'Engineering principles', 'Prototyping', 'Simulation', 'Mechanical systems', 'Technical drawings', 'Thermodynamics', 'Material science', 'Testing', 'Quality control', 'Project management', 'Automation', 'Problem-solving', 'Technical specifications', 'Machine design']),
    ('Nurse',['Nursing', 'Patient care', 'Medical procedures', 'Healthcare', 'Clinical skills', 'Emergency care', 'Patient assessment', 'Medication administration', 'Infection control', 'Wound care', 'Critical care', 'Health promotion', 'Health education', 'Documentation', 'Patient advocacy', 'Team collaboration', 'Patient safety', 'IV therapy', 'Disease management', 'Patient monitoring']),
    ('Graphic Designer', ['Graphic design', 'Adobe Creative Suite', 'Visual communication', 'Typography', 'Layout design', 'Brand identity', 'Print design', 'Digital design', 'Illustration', 'Logo design', 'User interface design', 'Color theory', 'Art direction', 'Creative concepting', 'Image editing', 'Multimedia design', 'Motion graphics', 'Web design', 'Packaging design', 'Graphic production']),
    ('sales', ['Sales', 'Business development', 'Relationship building', 'Prospecting', 'Lead generation', 'Negotiation', 'Customer acquisition', 'Client management', 'Sales targets', 'Closing deals', 'Sales strategies', 'Consultative selling', 'CRM', 'Presentation skills', 'Customer service', 'Sales forecasting', 'Cross-selling', 'Account management', 'Sales cycle', 'Sales techniques']),
    ('marketing', ['Marketing', 'Digital marketing', 'Social media', 'Content marketing', 'SEO', 'Email marketing', 'Marketing campaigns', 'Market research', 'Brand management', 'Marketing strategy', 'Advertising', 'Copywriting', 'Marketing analytics', 'CRM', 'Lead generation', 'Marketing automation', 'Campaign management', 'Public relations', 'Customer segmentation', 'Marketing ROI']),
    ('finance', ['Finance', 'Financial analysis', 'Accounting', 'Budgeting', 'Financial planning', 'Investment analysis', 'Risk management', 'Financial reporting', 'Financial modeling', 'Cash flow management', 'Financial forecasting', 'Cost analysis', 'Taxation', 'Auditing', 'Financial statements', 'Capital budgeting', 'Financial control', 'Financial regulations', 'Financial compliance', 'Corporate finance']),
    ('engineering', ['Engineering', 'Mechanical engineering', 'Electrical engineering', 'Civil engineering', 'Software engineering', 'Chemical engineering', 'Industrial engineering', 'Structural engineering', 'Engineering design', 'Engineering analysis', 'Technical drawings', 'CAD', 'Prototype development', 'Project management', 'Quality control', 'Process improvement', 'Problem-solving', 'Technical documentation', 'Product development', 'Innovation']),
    ('Content Strategist', ['Content strategy', 'Content planning', 'Content creation', 'Content marketing', 'Audience analysis', 'Content optimization', 'SEO', 'Content distribution', 'Content calendar', 'Content management', 'User experience', 'Copywriting', 'Content metrics', 'Content governance', 'Content workflow', 'Brand messaging', 'Content research', 'Storytelling', 'Information architecture', 'Content performance']),
    ('Mobile App Developer', ['Mobile app development', 'iOS development', 'Android development', 'Cross-platform development', 'Mobile UI', 'Mobile UX', 'Mobile app testing', 'Mobile app optimization', 'Backend integration', 'API development', 'Push notifications', 'Mobile app deployment', 'Mobile app security', 'Mobile app performance', 'Hybrid app development', 'Native app development', 'Mobile app frameworks', 'Mobile app design', 'Mobile app analytics', 'Mobile app maintenance']),
    ('Data Engineer', ['Data engineering', 'Data pipelines', 'Data integration', 'Data architecture', 'ETL', 'Data warehousing', 'Data modeling', 'Big data', 'Data ingestion', 'Data transformation', 'Data quality', 'Database management', 'Data migration', 'Cloud computing', 'Data governance', 'SQL', 'Data security', 'Streaming data', 'Data analytics', 'Data storage']),
    ('Administrative Assistant',['Administrative support', 'Calendar management', 'Meeting coordination', 'Travel arrangements', 'Correspondence', 'Document preparation', 'Email management', 'Data entry', 'File management', 'Office organization', 'Time management', 'Event planning', 'Scheduling', 'Customer service', 'Administrative tasks', 'Report generation', 'Invoicing', 'Office supplies management', 'Team coordination', 'Task prioritization']),
    ('Video Producer', ['Video production', 'Video editing', 'Storytelling', 'Scriptwriting', 'Cinematography', 'Video shooting', 'Post-production', 'Video direction', 'Storyboarding', 'Video marketing', 'Visual effects', 'Motion graphics', 'Video content strategy', 'Video project management', 'Video equipment', 'Audio editing', 'Color grading', 'Video distribution', 'Creative direction', 'Video storytelling']),
    ('Software Architect',['Software architecture', 'System design', 'Software development', 'Application architecture', 'Software frameworks', 'Technical leadership', 'Software scalability', 'Performance optimization', 'Software patterns', 'Code review', 'API design', 'Software documentation', 'Design patterns', 'Microservices architecture', 'Cloud architecture', 'Software security', 'Architecture standards', 'Software testing', 'Technical roadmaps', 'Agile methodologies']),
    ('Digital Marketing Manager', ['Digital marketing', 'Marketing strategy', 'Online advertising', 'Social media marketing', 'Search engine marketing', 'Email marketing', 'Content marketing', 'SEO', 'Google Analytics', 'Conversion rate optimization', 'Campaign management', 'Marketing automation', 'Social media management', 'Digital advertising', 'Marketing analytics', 'Digital strategy', 'Lead generation', 'Digital branding', 'Data-driven marketing', 'ROI analysis']),
    ('Human Resources Manager',['Human resources management', 'Employee relations', 'Talent acquisition', 'Performance management', 'Employee engagement', 'HR policies', 'Recruitment', 'Compensation management', 'Benefits administration', 'Training and development', 'Employee onboarding', 'HR compliance', 'Employee relations', 'Succession planning', 'HR strategy', 'Organizational development', 'HR metrics', 'HRIS', 'Employment law', 'Workforce planning']),
    ('Data Entry Clerk', ['Data entry', 'Data accuracy', 'Data verification', 'Data management', 'Data processing', 'Data cleansing', 'Data organization', 'Typing speed', 'Attention to detail', 'Excel', 'Data analysis', 'Data reporting', 'Data integrity', 'Data confidentiality', 'Quality control', 'Information management', 'Time management', 'Data entry software', 'Data entry tools', 'Database management']),
    ('Cloud Solutions Architect', ['Cloud solutions', 'Cloud architecture', 'Cloud migration', 'Cloud computing', 'Infrastructure as a Service (IaaS)', 'Platform as a Service (PaaS)', 'Software as a Service (SaaS)', 'Cloud security', 'Cloud storage', 'Serverless architecture', 'Containerization', 'Microservices', 'Cloud deployment', 'Cloud scalability', 'Cloud automation', 'Cloud cost optimization', 'Cloud networking', 'High availability', 'Disaster recovery', 'Cloud governance']),
    ('Technical Writer', ['Technical writing', 'Technical documentation', 'User manuals', 'API documentation', 'Software documentation', 'Technical communication', 'Technical editing', 'Information architecture', 'Writing style guides', 'Knowledge base', 'White papers', 'Instructional design', 'Content management systems', 'Document versioning', 'Documentation standards', 'Gathering requirements', 'Technical illustrations', 'Writing guidelines', 'Editing and proofreading', 'API references']),
    ('Business Intelligence Analyst',['Business intelligence', 'Data analysis', 'Data visualization', 'Data modeling', 'Business analytics', 'Data mining', 'Dashboard development', 'Data reporting', 'Data interpretation', 'Key performance indicators (KPIs)', 'Data-driven decision-making', 'SQL', 'Business insights', 'Data warehouse', 'Data extraction', 'Data manipulation', 'Business dashboards', 'BI tools', 'Data storytelling', 'Predictive analytics']),
    ('Customer Success Manager', ['Customer success', 'Customer relationship management', 'Customer satisfaction', 'Account management', 'Client onboarding', 'Customer retention', 'Customer support', 'Customer engagement', 'Customer advocacy', 'Renewal management', 'Upselling', 'Cross-selling', 'Churn reduction', 'Customer feedback', 'Customer needs analysis', 'Relationship building', 'Training and onboarding', 'Customer success metrics', 'Customer success strategies', 'Customer success software']),
    ('Back-end Developer', ['Java', 'Python', 'API development', 'Web servers', 'Database management','Back-end development', 'Server-side programming', 'API development', 'Database management', 'Web development frameworks', 'RESTful APIs', 'Data modeling', 'Server-side scripting', 'Server management', 'Database querying', 'Security protocols', 'Performance optimization', 'Code optimization', 'Version control', 'Server deployment', 'Back-end testing', 'Back-end architecture', 'Back-end frameworks', 'System integration', 'Scalability']),
    ('UI/UX Developer', ['Back-end development', 'Server-side programming', 'API development', 'Database management', 'Web development frameworks', 'RESTful APIs', 'Data modeling', 'Server-side scripting', 'Server management', 'Database querying', 'Security protocols', 'Performance optimization', 'Code optimization', 'Version control', 'Server deployment', 'Back-end testing', 'Back-end architecture', 'Back-end frameworks', 'System integration', 'Scalability', 'HTML', 'CSS']),
    ('Product Manager', ['Product management', 'Product strategy', 'Product roadmap', 'Market research', 'User research', 'Product development', 'Agile methodologies', 'Scrum', 'Product requirements', 'Product launch', 'Competitor analysis', 'User stories', 'Product pricing', 'Product positioning', 'Product marketing', 'Product analytics', 'Product lifecycle', 'Product vision', 'Cross-functional collaboration', 'Product success metrics']),
    ('Technical Support Engineer', ['Technical support', 'Troubleshooting', 'Issue resolution', 'Customer support', 'Problem-solving', 'Ticketing systems', 'Remote support', 'Product knowledge', 'Technical documentation', 'Hardware support', 'Software support', 'Customer communication', 'Escalation management', 'Bug tracking', 'Root cause analysis', 'Technical training', 'Technical expertise', 'System configuration', 'Customer satisfaction', 'Service level agreements (SLAs)']),
    ('Sales Manager', ['Sales management', 'Sales strategy', 'Business development', 'Sales planning', 'Sales forecasting', 'Sales team management', 'Sales targets', 'Customer acquisition', 'Account management', 'Lead generation', 'Sales pipeline management', 'Sales negotiations', 'Relationship building', 'Sales presentations', 'Sales analytics', 'Sales performance', 'CRM', 'Sales process', 'Sales training', 'Competitive analysis']),
    ('SEO Specialist', ['SEO', 'Search engine optimization', 'Keyword research', 'On-page optimization', 'Off-page optimization', 'Link building', 'SEO analysis', 'SEO tools', 'Google Analytics', 'Search engine rankings', 'SEO strategy', 'SEO audits', 'SEO reporting', 'SEO trends', 'Website optimization', 'Meta tags', 'Content optimization', 'Technical SEO', 'SEO performance', 'SEO best practices']),
    ('SEO Specialist', ['SEO', 'Search engine optimization', 'Keyword research', 'On-page optimization', 'Off-page optimization', 'Link building', 'SEO analysis', 'SEO tools', 'Google Analytics', 'Search engine rankings', 'SEO strategy', 'SEO audits', 'SEO reporting', 'SEO trends', 'Website optimization', 'Meta tags', 'Content optimization', 'Technical SEO', 'SEO performance', 'SEO best practices']),
    ('Operations Manager', ['Operations management', 'Process improvement', 'Project management', 'Strategic planning', 'Budget management', 'Resource allocation', 'Risk management', 'Performance metrics', 'Quality control', 'Supply chain management', 'Inventory management', 'Workflow optimization', 'Cross-functional collaboration', 'Continuous improvement', 'Change management', 'Operations efficiency', 'Lean methodologies', 'Business processes', 'Operations strategy', 'Operational excellence'])
'''
#]

# Create training data
train_data = []
for category, keywords in categories:
    for keyword in keywords:
        train_data.append((keyword, category))
print(train_data)
# Train the classifier
classifier = NaiveBayesClassifier(train_data)

# Test the classifier
test_data = [
    'We need a developer with experience in Java, Spring framework and debugging',
    'Person  needed for developing new marketing strategy',
    'In search of a person with experience in making deals and good negotiation skills',
    'Required person who coordinate and take care of patient, their medication',
]
for job_title in test_data:
    category = classifier.classify(job_title)
    print(f"{job_title} is in the {category} category.")
