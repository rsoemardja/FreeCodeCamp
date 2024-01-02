class Application extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      markdown: placeholder
    };
    this.handleChange = this.handleChange.bind(this);
  }
  handleChange(e) {
    this.setState({
      markdown: e.target.value
    });
  }
  render() {
    return (
      <div>
        <div className="row">
          <div className="col-md-6">
            <h1>Editor</h1>
            <textarea
              id="editor"
              className="form-control"
              value={this.state.markdown}
              onChange={this.handleChange}
            />
          </div>
          <div className="col-md-6">
            <h1>Preview</h1>
            <div
              id="preview"
              dangerouslySetInnerHTML={{
                __html: marked(this.state.markdown)
              }}
            />
          </div>
        </div>
      </div>
    );
  }
}