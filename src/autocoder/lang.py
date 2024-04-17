lang_desc = {
    "en": {
        "parser_desc": "Auto-implement missing methods in a Python script.",
        "source_dir": "Path to the project source code directory",
        "git_url": "URL of the git repository to clone the source code from",
        "target_file": "The file path to write the generated source code to",
        "query": "The user query or instruction to handle the source code",
        "template": "The template to use for generating the source code. Default is 'common'",
        "project_type": "The type of the project. Options: py, ts, py-script, translate, or file suffix. Default is 'py'",
        "execute": "Whether to execute the generated code. Default is False",
        "package_name": "Only works for py-script project type. The package name of the script. Default is empty.",
        "script_path": "Only works for py-script project type. The path to the Python script. Default is empty.",
        "model": "The name of the model to use. Default is empty",
        "model_max_length": "The maximum length of the generated code by the model. Default is 1024. This only works when model is specified.",
        "file": "Path to the YAML configuration file",
        "anti_quota_limit": "Time to wait in seconds after each API request. Default is 1s",
        "skip_build_index": "Whether to skip building the source code index. Default is False",
        "print_request": "Whether to print the request sent to the model. Default is False",
        "cmd_args_title": "Command Line Arguments:",
        "py_packages": "The Python packages added to context, only works for py project type. Default is empty.",
        "human_as_model": "Use human as model or not. Default is False",
        "urls": "The urls to crawl and extract text from, separated by comma",
        "search_engine": "The search engine to use. Supported engines: bing, google. Default is empty",
        "search_engine_token": "The token for the search engine API. Default is empty",
        "model_max_input_length": "The maximum length of the generated code by the model. Default is 6000. This only works when model is specified.",
        "auto_merge": "Whether to automatically merge the generated code into the existing file. Default is False",
        "revert_desc": "Revert the changes made by the specified file",
        "vl_model": "The name of the multi-modal model to use. Default is empty",
        "sd_model": "The name of the stable diffusion model to use. Default is empty",
        "emb_model": "The name of the embedding model to use. Default is empty",
        "index_model": "The name of the model used to build index. Default is empty",
         "image_file": "The path of the image file to process. Default is empty",
        "index_desc": "Build the source code index",  
        "index_query_desc": "Query related files based on the index"  ,
        "index_filter_level": "Index filter level, 0: only filter the file names mentioned in query, 1. filter the file names mentioned in query and possibly implicitly used files 2. files obtained from 0,1 and then find files related to these files",
        "store_desc": "Some statistics, such as token usage, etc.",
        "index_filter_workers": "Number of workers to use for filtering files by index",
        "image_max_iter": "The maximum number of iterations for image to html. Default is 1",
        "doc_desc": "Some operation on doc,e.g. extract text from html",
        "urls_use_model":"Whether to use model to processing content in urls. Default is False",
        "ray_address": "The address of the Ray cluster to connect to. Default is 'auto'",        
    },
    "zh": {
        "parser_desc": "自动为Python脚本实现缺失的方法。",
        "source_dir": "项目源代码目录路径",
        "git_url": "用于克隆源代码的Git仓库URL",
        "target_file": "生成的源代码的输出文件路径",
        "query": "用户查询或处理源代码的指令",
        "template": "生成源代码使用的模板。默认为'common'",
        "project_type": "项目类型。可选值:py、ts、py-script、translate或文件后缀名。默认为'py'",
        "execute": "是否执行生成的代码。默认为False",
        "package_name": "仅适用于py-script项目类型。脚本的包名。默认为空。",
        "script_path": "仅适用于py-script项目类型。Python脚本路径。默认为空。",
        "model": "使用的模型名称。默认为空",
        "model_max_length": "模型生成代码的最大长度。默认为1024。仅在指定模型时生效。",
        "file": "YAML配置文件路径",
        "anti_quota_limit": "每次API请求后等待的秒数。默认为1秒",
        "skip_build_index": "是否跳过构建源代码索引。默认为False",
        "print_request": "是否打印发送到模型的请求。默认为False",
        "cmd_args_title": "命令行参数:",
        "py_packages": "添加到上下文的Python包,仅适用于py项目类型。默认为空。",
        "human_as_model": "是否使用人工作为模型。默认为False",
        "urls": "要爬取并提取文本的URL,多个URL以逗号分隔",
        "search_engine": "要使用的搜索引擎。支持的引擎:bing、google。默认为空",
        "search_engine_token": "搜索引擎API的令牌。默认为空",
        "model_max_input_length": "模型的最大输入长度。默认为6000。仅在指定模型时生效。",
        "auto_merge": "是否自动将生成的代码合并到现有文件中。默认为False。",
        "revert_desc": "撤销指定文件所做的更改",
        "vl_model": "要使用的多模态模型的名称。默认为空",
        "sd_model": "要使用的稳定扩散模型的名称。默认为空",
        "emb_model": "要使用的嵌入模型的名称。默认为空",
        "index_model": "用于构建索引的模型名称。默认为空",
         "image_file": "要处理的图像文件路径。默认为空",
        "index_desc": "构建源代码索引",
        "index_query_desc": "根据索引查询相关文件",
        "index_filter_level": "索引过滤级别,0:仅过滤query 中提到的文件名，1. 过滤query 中提到的文件名以及可能会隐含会使用的文件 2. 从0,1 中获得的文件，再寻找这些文件相关的文件。",        
        "store_desc": "一些统计信息，比如token使用等",
        "index_filter_workers":"用于通过索引过滤文件的工作线程数",
        "image_max_iter": "图像转html的最大迭代次数。默认为1",
        "doc_desc": "对文档进行一些操作,诸如获取html的正文内容",
        "urls_use_model":"是否使用模型处理urls中的内容。默认为False",
        "ray_address": "要连接的Ray集群的地址。默认为'auto'",
    }
}