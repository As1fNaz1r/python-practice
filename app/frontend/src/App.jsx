import { useState, useEffect } from 'react'
import Prism from 'prismjs'
import 'prismjs/themes/prism-tomorrow.css'
import 'prismjs/components/prism-python'
import 'prismjs/components/prism-markdown'
import './App.css'

const API_URL = 'http://localhost:8000'

// SVG Icons as components
const SearchIcon = () => (
  <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round">
    <circle cx="11" cy="11" r="8"/>
    <path d="m21 21-4.35-4.35"/>
  </svg>
)
const FolderOpenIcon = () => (
  <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round">
    <path d="M22 19a2 2 0 0 1-2 2H4a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h5l2 3h9a2 2 0 0 1 2 2z"/>
    <line x1="12" y1="11" x2="12" y2="17"/>
    <line x1="9" y1="14" x2="15" y2="14"/>
  </svg>
)

const FolderClosedIcon = () => (
  <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round">
    <path d="M22 19a2 2 0 0 1-2 2H4a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h5l2 3h9a2 2 0 0 1 2 2z"/>
  </svg>
)

const FileIcon = ({ ext }) => {
  if (ext === 'py') {
    return (
      <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="#22c55e" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round">
        <path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/>
        <polyline points="14 2 14 8 20 8"/>
        <line x1="16" y1="13" x2="8" y2="13"/>
        <line x1="16" y1="17" x2="8" y2="17"/>
        <polyline points="10 9 9 9 8 9"/>
      </svg>
    )
  }
  return (
    <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="#fcd34d" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round">
      <path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/>
      <polyline points="14 2 14 8 20 8"/>
      <line x1="16" y1="13" x2="8" y2="13"/>
      <line x1="16" y1="17" x2="8" y2="17"/>
    </svg>
  )
}

const CopyIcon = () => (
  <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round">
    <rect x="9" y="9" width="13" height="13" rx="2" ry="2"/>
    <path d="M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1"/>
  </svg>
)

const CheckIcon = () => (
  <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round">
    <polyline points="20 6 9 17 4 12"/>
  </svg>
)

function FolderItem({ item, level = 0, onSelect, selectedFile }) {
  const [expanded, setExpanded] = useState(false)
  const paddingLeft = `${level * 20 + 12}px`

  if (item.type === 'folder') {
    return (
      <div className="folder-item">
        <div 
          className="folder-header"
          style={{ paddingLeft }}
          onClick={() => setExpanded(!expanded)}
        >
          <span className="folder-icon">{expanded ? <FolderOpenIcon /> : <FolderClosedIcon />}</span>
          <span className="folder-name">{item.name}</span>
        </div>
        {expanded && (
          <div className="folder-children">
            {item.children.map((child, idx) => (
              <FolderItem 
                key={idx} 
                item={child} 
                level={level + 1}
                onSelect={onSelect}
                selectedFile={selectedFile}
              />
            ))}
          </div>
        )}
      </div>
    )
  }

  return (
    <button
      className={`file-btn ${selectedFile === item.path ? 'active' : ''}`}
      style={{ paddingLeft }}
      onClick={() => onSelect(item)}
    >
      <FileIcon ext={item.language} />
      <span>{item.name}</span>
    </button>
  )
}

function TopicSection({ topic, onSelect, selectedFile }) {
  const [expanded, setExpanded] = useState(false)

  return (
    <div key={topic.id} className="topic">
      <div 
        className="topic-header"
        onClick={() => setExpanded(!expanded)}
      >
        <span>{expanded ? '▼' : '▶'}</span>
        <h3>{topic.name}</h3>
      </div>
      
      {expanded && (
        <div className="topic-content">
          {topic.docs && (
            <div className="topic-docs">{topic.docs}</div>
          )}
          <div className="folder-tree">
            {topic.structure.map((item, idx) => (
              <FolderItem 
                key={idx} 
                item={item} 
                onSelect={onSelect}
                selectedFile={selectedFile}
              />
            ))}
          </div>
        </div>
      )}
    </div>
  )
}

function CodeViewer({ fileContent }) {
  const [copied, setCopied] = useState(false)

  useEffect(() => {
    if (fileContent?.content) {
      Prism.highlightAll()
    }
  }, [fileContent])

  const handleCopy = async () => {
    if (fileContent?.content) {
      await navigator.clipboard.writeText(fileContent.content)
      setCopied(true)
      setTimeout(() => setCopied(false), 2000)
    }
  }

  if (!fileContent) return null

  const languageClass = fileContent.language === 'py' ? 'python' : fileContent.language === 'md' ? 'markdown' : 'text'

  return (
    <div className="file-viewer">
      <div className="file-header">
        <div className="file-info">
          <FileIcon ext={fileContent.language} />
          <div className="file-details">
            <h2>{fileContent.name}</h2>
            <span className="file-path">{fileContent.path.replace(/\//g, ' / ')}</span>
          </div>
        </div>
        <div className="file-actions">
          <button 
            className={`action-btn ${copied ? 'copied' : ''}`}
            onClick={handleCopy}
          >
            {copied ? <CheckIcon /> : <CopyIcon />}
            {copied ? 'Copied!' : 'Copy'}
          </button>
        </div>
      </div>
      <div className="code-container">
        <pre className="code">
          <code className={`language-${languageClass}`}>{fileContent.content}</code>
        </pre>
      </div>
    </div>
  )
}

function App() {
  const [topics, setTopics] = useState([])
  const [selectedFile, setSelectedFile] = useState(null)
  const [fileContent, setFileContent] = useState(null)
  const [stats, setStats] = useState(null)
  const [activeTab, setActiveTab] = useState('topics')
  const [loading, setLoading] = useState(true)
  const [searchQuery, setSearchQuery] = useState('')
  const [searchResults, setSearchResults] = useState([])
  const [searching, setSearching] = useState(false)

  useEffect(() => {
    fetchTopics()
    fetchStats()
  }, [])

  useEffect(() => {
    const timer = setTimeout(() => {
      if (searchQuery.length >= 2) {
        performSearch()
      } else {
        setSearchResults([])
      }
    }, 300)
    return () => clearTimeout(timer)
  }, [searchQuery])

  const fetchTopics = async () => {
    try {
      const res = await fetch(`${API_URL}/api/topics`)
      const data = await res.json()
      setTopics(data)
      setLoading(false)
    } catch (err) {
      console.error('Error fetching topics:', err)
      setLoading(false)
    }
  }

  const fetchStats = async () => {
    try {
      const res = await fetch(`${API_URL}/api/stats`)
      const data = await res.json()
      setStats(data)
    } catch (err) {
      console.error('Error fetching stats:', err)
    }
  }

  const fetchFile = async (file) => {
    try {
      const res = await fetch(`${API_URL}/api/file/${file.path}`)
      const data = await res.json()
      setFileContent(data)
      setSelectedFile(file.path)
    } catch (err) {
      console.error('Error fetching file:', err)
    }
  }

  const performSearch = async () => {
    setSearching(true)
    try {
      const res = await fetch(`${API_URL}/api/search?q=${encodeURIComponent(searchQuery)}`)
      const data = await res.json()
      setSearchResults(data.results || [])
    } catch (err) {
      console.error('Error searching:', err)
      setSearchResults([])
    } finally {
      setSearching(false)
    }
  }

  return (
    <div className="app">
      <header className="header">
        <h1>🐍 Python Practice Dashboard</h1>
        <p>Review your learning journey</p>
      </header>

      <div className="tabs">
        <button 
          className={activeTab === 'topics' ? 'active' : ''} 
          onClick={() => setActiveTab('topics')}
        >
          Topics
        </button>
        <button 
          className={activeTab === 'stats' ? 'active' : ''} 
          onClick={() => setActiveTab('stats')}
        >
          Stats
        </button>
        <button 
          className={activeTab === 'search' ? 'active' : ''} 
          onClick={() => setActiveTab('search')}
        >
          Search
        </button>
      </div>

      <div className="container">
        {activeTab === 'topics' && (
          <div className="content">
            <aside className="sidebar">
              <h2>Topics</h2>
              {loading ? (
                <div className="loading">
                  <div className="spinner" />
                  <p>Loading topics...</p>
                </div>
              ) : (
                topics.map(topic => (
                  <TopicSection 
                    key={topic.id} 
                    topic={topic}
                    onSelect={fetchFile}
                    selectedFile={selectedFile}
                  />
                ))
              )}
            </aside>

            <main className="main">
              {fileContent ? (
                <CodeViewer fileContent={fileContent} />
              ) : (
                <div className="placeholder">
                  <div className="placeholder-icon">📁</div>
                  <h2>Select a file to view</h2>
                  <p>Choose a topic and file from the sidebar</p>
                </div>
              )}
            </main>
          </div>
        )}

        {activeTab === 'stats' && stats && (
          <div className="stats-view">
            <div className="stat-card">
              <h3>Total Files</h3>
              <div className="stat-value">{stats.total_files}</div>
            </div>
            
            <div className="stat-card">
              <h3>Python Files</h3>
              <div className="stat-value">{stats.by_type.python || 0}</div>
            </div>
            
            <div className="stat-card">
              <h3>Markdown Files</h3>
              <div className="stat-value">{stats.by_type.markdown || 0}</div>
            </div>

            <div className="stat-card">
              <h3>Total Lines</h3>
              <div className="stat-value">{stats.total_lines?.toLocaleString() || 0}</div>
            </div>

            <div className="topics-breakdown">
              <h3>Topics Breakdown</h3>
              {stats.topics.map(topic => (
                <div key={topic.name} className="topic-stat">
                  <span className="topic-name">{topic.name}</span>
                  <div className="topic-counts">
                    <span className="count">{topic.python_files} .py</span>
                    <span className="count">{topic.markdown_files} .md</span>
                    <span className="count">{topic.lines?.toLocaleString() || 0} lines</span>
                  </div>
                </div>
              ))}
            </div>
          </div>
        )}

        {activeTab === 'search' && (
          <div className="search-view">
            <div className="search-container">
              <div className="search-box">
                <SearchIcon />
                <input
                  type="text"
                  placeholder="Search files by name or content..."
                  value={searchQuery}
                  onChange={(e) => setSearchQuery(e.target.value)}
                  autoFocus
                />
              </div>
              
              {searching && (
                <div className="loading">
                  <div className="spinner" />
                  <p>Searching...</p>
                </div>
              )}

              {!searching && searchQuery.length >= 2 && (
                <div className="search-results">
                  {searchResults.length === 0 ? (
                    <div className="no-results">
                      <p>No results found for "{searchQuery}"</p>
                    </div>
                  ) : (
                    <>
                      <div className="results-header">
                        <p>{searchResults.length} result{searchResults.length !== 1 ? 's' : ''} found</p>
                      </div>
                      {searchResults.map((result, idx) => (
                        <div 
                          key={idx} 
                          className="search-result-item"
                          onClick={() => fetchFile(result)}
                        >
                          <FileIcon ext={result.language} />
                          <div className="result-info">
                            <div className="result-name">{result.name}</div>
                            <div className="result-path">{result.path}</div>
                            {result.preview && (
                              <div className="result-preview">{result.preview}</div>
                            )}
                            {result.line && (
                              <div className="result-line">Line {result.line}</div>
                            )}
                          </div>
                        </div>
                      ))}
                    </>
                  )}
                </div>
              )}

              {searchQuery.length < 2 && (
                <div className="search-hint">
                  <p>Type at least 2 characters to search</p>
                </div>
              )}
            </div>
          </div>
        )}
      </div>
    </div>
  )
}

export default App