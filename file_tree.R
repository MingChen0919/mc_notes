file_tree = function(dir = '.'){
  # # get the OUTPUT_DIR folder data: dataset_NUMBER_files
  # report_files_path = Sys.getenv('REPORT_FILES_PATH')
  # output_dir = tail(strsplit(report_files_path, '/')[[1]], 1)
  
  files = list.files(path = dir, recursive = FALSE, full.names = TRUE)
  # files also include directorys, need to remove directorys
  files = files[!dir.exists(files)]
  dirs = list.dirs(path = dir, recursive = FALSE, full.names = TRUE)
  # exclude .ipynb_checkpoints folder
  # ipynb_checkpoints = grep(pattern = 'ipynb_checkpoints', x = dirs)
  # dirs = dirs[-ipynb_checkpoints]
  
  tags$ul(
    {
      if (length(files) > 0) {
        lapply(files, function(x){
          path_end = tail(strsplit(x, '/')[[1]],1)
          li_item = tags$li(tags$a(path_end, href=paste0(params$github_repo_url, x)))
          li_item$attribs = list('data-jstree'='{"icon":"jstree-file"}')
          li_item
        })
      }
    },
    {
      if (length(dirs) > 0) {
        lapply(dirs, function(x){
          path_end = tail(strsplit(x, '/')[[1]],1)
          if (!(path_end %in% strsplit(params$hidden_folders, ','))) {
            li_item = tags$li(path_end, file_tree(x))
            li_item$attribs = list('data-jstree' = '{"icon":"jstree-folder"}', class=list('jstree-open'))
            li_item
          }
        })
      }
    }
  )
}